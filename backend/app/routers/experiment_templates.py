import shutil
from datetime import datetime, timezone
from typing import Any

from beanie import PydanticObjectId, operators
from beanie.odm.operators.find.comparison import Eq
from beanie.odm.operators.find.evaluation import Text
from beanie.odm.queries.find import FindMany
from fastapi import APIRouter, Depends, HTTPException, status

from app.authentication import get_current_user
from app.config import settings
from app.helpers import Pagination, QueryOperator, get_compare_operator_fn
from app.models.experiment import Experiment
from app.models.experiment_template import ExperimentTemplate
from app.schemas.experiment_template import (
    ExperimentTemplateCreate,
    ExperimentTemplateResponse,
)
from app.schemas.states import TemplateState
from app.services.experiment_scheduler import ExperimentScheduler

router = APIRouter()


@router.get("/experiment-templates", response_model=list[ExperimentTemplateResponse])
async def get_experiment_templates(
    user: dict = Depends(get_current_user(required=False)),
    query: str = "",
    pagination: Pagination = Depends(),
    mine: bool | None = None,
    finalized: bool | None = None,
    approved: bool | None = None,
    archived: bool | None = None,
    public: bool | None = None,
) -> Any:
    result_set = find_specific_experiment_templates(
        query,
        mine=mine,
        finalized=finalized,
        approved=approved,
        archived=archived,
        public=public,
        user=user,
        pagination=pagination,
    )
    experiment_templates = await result_set.to_list()

    return [
        experiment_template.map_to_response(user)
        for experiment_template in experiment_templates
    ]


@router.get("/experiment-templates/{id}", response_model=ExperimentTemplateResponse)
async def get_experiment_template(
    id: PydanticObjectId, user: dict = Depends(get_current_user(required=False))
) -> Any:
    experiment_template = await get_experiment_template_if_accessible_or_raise(id, user)
    return experiment_template.map_to_response(user)


@router.get("/count/experiment-templates", response_model=int)
async def get_experiment_templates_count(
    user: dict = Depends(get_current_user(required=False)),
    query: str = "",
    mine: bool | None = None,
    finalized: bool | None = None,
    approved: bool | None = None,
    archived: bool | None = None,
    public: bool | None = None,
) -> Any:
    result_set = find_specific_experiment_templates(
        query,
        mine=mine,
        finalized=finalized,
        approved=approved,
        archived=archived,
        public=public,
        user=user,
    )
    return await result_set.count()


@router.post(
    "/experiment-templates",
    status_code=status.HTTP_201_CREATED,
    response_model=ExperimentTemplateResponse,
)
async def create_experiment_template(
    experiment_template: ExperimentTemplateCreate,
    user: dict = Depends(get_current_user(required=True)),
) -> Any:
    experiment_template_obj = ExperimentTemplate(
        **experiment_template.dict(), created_by=user["email"]
    )
    experiment_template_obj = await experiment_template_obj.create()

    experiment_template_obj.initialize_files(
        base_image=experiment_template.base_image,
        pip_requirements=experiment_template.pip_requirements,
        script=experiment_template.script,
    )
    return experiment_template_obj.map_to_response(user)


@router.put("/experiment-templates/{id}", response_model=ExperimentTemplateResponse)
async def update_experiment_template(
    id: PydanticObjectId,
    experiment_template: ExperimentTemplateCreate,
    user: dict = Depends(get_current_user(required=True)),
) -> Any:
    original_template = await get_experiment_template_if_accessible_or_raise(
        id, user, write_access=True
    )
    has_experiments = (
        await Experiment.find(Experiment.experiment_template_id == id).count() > 0
    )
    has_experiments_of_others = (
        await Experiment.find(
            Experiment.experiment_template_id == id,
            Experiment.created_by != user["email"],
        ).count()
        > 0
    )

    template_to_save = await ExperimentTemplate.update_template(
        original_template,
        experiment_template,
        editable_environment=has_experiments is False,
        editable_visibility=has_experiments_of_others is False,
    )
    if template_to_save is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Performed changes to the experiment template are not allowed",
        )

    await ExperimentTemplate.replace(template_to_save)
    return template_to_save.map_to_response(user)


@router.delete("/experiment-templates/{id}", response_model=None)
async def remove_experiment_template(
    id: PydanticObjectId, user: dict = Depends(get_current_user(required=True))
) -> Any:
    await get_experiment_template_if_accessible_or_raise(id, user, write_access=True)
    exist_experiments = (
        await Experiment.find(Experiment.experiment_template_id == id).count() > 0
    )
    if exist_experiments:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This experiment template cannot be deleted.",
        )

    shutil.rmtree(settings.get_experiment_template_path(id))
    await ExperimentTemplate.find(ExperimentTemplate.id == id).delete()


@router.patch("/experiment-templates/{id}/archive", response_model=None)
async def archive_experiment_template(
    id: PydanticObjectId,
    archived: bool = False,
    user: dict = Depends(get_current_user(required=True)),
) -> Any:
    experiment_template = await get_experiment_template_if_accessible_or_raise(
        id, user, write_access=True
    )
    experiment_template.archived = archived

    await ExperimentTemplate.replace(experiment_template)


@router.patch("/experiment-templates/{id}/approve", response_model=None)
async def approve_experiment_template(
    id: PydanticObjectId,
    password: str,
    approved: bool = False,
    exp_scheduler: ExperimentScheduler = Depends(ExperimentScheduler.get_service),
) -> Any:
    if password != settings.PASSWORD_FOR_TEMPLATE_APPROVAL:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong password given",
        )

    experiment_template = await ExperimentTemplate.get(id)
    if experiment_template is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Such experiment template doesn't exist",
        )

    experiment_template.approved = approved
    experiment_template.updated_at = datetime.now(tz=timezone.utc)
    await ExperimentTemplate.replace(experiment_template)

    if approved:
        await exp_scheduler.add_image_to_build(experiment_template.id)


@router.get("/count/experiment-templates/{id}/experiments", response_model=int)
async def get_experiments_of_template_count(
    id: PydanticObjectId,
    only_mine: bool = False,
    user: dict = Depends(get_current_user(required=True)),
) -> Any:
    await get_experiment_template_if_accessible_or_raise(id, user)

    search_conditions = [Experiment.created_by == user["email"]] if only_mine else []
    search_conditions.append(Experiment.experiment_template_id == id)

    return await Experiment.find(*search_conditions).count()


def find_specific_experiment_templates(
    search_query: str,
    mine: bool | None,
    finalized: bool | None,
    approved: bool | None,
    archived: bool | None,
    public: bool | None,
    user: dict | None,
    query_operator: QueryOperator = QueryOperator.AND,
    pagination: Pagination = None,
) -> FindMany[ExperimentTemplate]:
    page_kwargs = (
        {"skip": pagination.offset, "limit": pagination.limit}
        if pagination is not None
        else {}
    )
    # initial condition -> retrieve only those objects that are accessible to a user
    search_conditions = [
        operators.Or(
            ExperimentTemplate.public == True,  # noqa: E712
            Eq(
                ExperimentTemplate.created_by, user["email"] if user is not None else ""
            ),
        )
    ]

    # applying filters
    if len(search_query) > 0:
        search_conditions.append(Text(search_query))
    if mine is not None:
        if user is not None:
            search_conditions.append(
                get_compare_operator_fn(mine)(Experiment.created_by, user["email"])
            )
        else:
            # Authentication required to see your experiment templates
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="This endpoint requires authorization. You need to be logged in.",
                headers={"WWW-Authenticate": "Bearer"},
            )

    if finalized is not None:
        search_conditions.append(
            get_compare_operator_fn(finalized)(
                ExperimentTemplate.state, TemplateState.FINISHED
            )
        )
    if approved is not None:
        search_conditions.append(ExperimentTemplate.approved == approved)
    if archived is not None:
        search_conditions.append(ExperimentTemplate.archived == archived)
    if public is not None:
        search_conditions.append(ExperimentTemplate.public == public)

    multi_query = (
        operators.Or(*search_conditions)
        if query_operator == QueryOperator.OR
        else operators.And(*search_conditions)
    )
    return ExperimentTemplate.find(multi_query, **page_kwargs)


async def get_experiment_template_if_accessible_or_raise(
    template_id: PydanticObjectId, user: dict | None, write_access: bool = False
) -> ExperimentTemplate:
    access_denied_error = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="You cannot access this experiment template",
    )
    template = await ExperimentTemplate.get(template_id)

    if template is None:
        raise access_denied_error
    else:
        # Public templates are readable by everyone
        if write_access is False and template.public:
            return template
        # TODO: Add experiment template access management
        elif user is not None and template.created_by == user["email"]:
            return template
        else:
            return access_denied_error
