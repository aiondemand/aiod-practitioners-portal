# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

from app.schemas.aiod_generated.aio_d_entry_create import AIoDEntryCreate
from app.schemas.aiod_generated.distribution import Distribution
from app.schemas.aiod_generated.runnable_distribution import RunnableDistribution


class ExperimentCreate(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ExperimentCreate - a model defined in OpenAPI

        platform: The platform of this ExperimentCreate [Optional].
        platform_identifier: The platform_identifier of this ExperimentCreate [Optional].
        name: The name of this ExperimentCreate.
        description: The description of this ExperimentCreate [Optional].
        same_as: The same_as of this ExperimentCreate [Optional].
        date_published: The date_published of this ExperimentCreate [Optional].
        is_accessible_for_free: The is_accessible_for_free of this ExperimentCreate [Optional].
        version: The version of this ExperimentCreate [Optional].
        pid: The pid of this ExperimentCreate [Optional].
        experimental_workflow: The experimental_workflow of this ExperimentCreate [Optional].
        execution_settings: The execution_settings of this ExperimentCreate [Optional].
        reproducibility_explanation: The reproducibility_explanation of this ExperimentCreate [Optional].
        aiod_entry: The aiod_entry of this ExperimentCreate [Optional].
        alternate_name: The alternate_name of this ExperimentCreate [Optional].
        application_area: The application_area of this ExperimentCreate [Optional].
        badge: The badge of this ExperimentCreate [Optional].
        citation: The citation of this ExperimentCreate [Optional].
        contact: The contact of this ExperimentCreate [Optional].
        creator: The creator of this ExperimentCreate [Optional].
        distribution: The distribution of this ExperimentCreate [Optional].
        has_part: The has_part of this ExperimentCreate [Optional].
        industrial_sector: The industrial_sector of this ExperimentCreate [Optional].
        is_part_of: The is_part_of of this ExperimentCreate [Optional].
        keyword: The keyword of this ExperimentCreate [Optional].
        license: The license of this ExperimentCreate [Optional].
        media: The media of this ExperimentCreate [Optional].
        note: The note of this ExperimentCreate [Optional].
        research_area: The research_area of this ExperimentCreate [Optional].
        scientific_domain: The scientific_domain of this ExperimentCreate [Optional].
    """

    platform: Optional[str] = Field(alias="platform", default=None)
    platform_identifier: Optional[str] = Field(
        alias="platform_identifier", default=None
    )
    name: str = Field(alias="name")
    description: Optional[str] = Field(alias="description", default=None)
    same_as: Optional[str] = Field(alias="same_as", default=None)
    date_published: Optional[datetime] = Field(alias="date_published", default=None)
    is_accessible_for_free: Optional[bool] = Field(
        alias="is_accessible_for_free", default=None
    )
    version: Optional[str] = Field(alias="version", default=None)
    pid: Optional[str] = Field(alias="pid", default=None)
    experimental_workflow: Optional[str] = Field(
        alias="experimental_workflow", default=None
    )
    execution_settings: Optional[str] = Field(alias="execution_settings", default=None)
    reproducibility_explanation: Optional[str] = Field(
        alias="reproducibility_explanation", default=None
    )
    aiod_entry: Optional[AIoDEntryCreate] = Field(alias="aiod_entry", default=None)
    alternate_name: Optional[List[str]] = Field(alias="alternate_name", default=None)
    application_area: Optional[List[str]] = Field(
        alias="application_area", default=None
    )
    badge: Optional[List[str]] = Field(alias="badge", default=None)
    citation: Optional[List[int]] = Field(alias="citation", default=None)
    contact: Optional[List[int]] = Field(alias="contact", default=None)
    creator: Optional[List[int]] = Field(alias="creator", default=None)
    distribution: Optional[List[RunnableDistribution]] = Field(
        alias="distribution", default=None
    )
    has_part: Optional[List[int]] = Field(alias="has_part", default=None)
    industrial_sector: Optional[List[str]] = Field(
        alias="industrial_sector", default=None
    )
    is_part_of: Optional[List[int]] = Field(alias="is_part_of", default=None)
    keyword: Optional[List[str]] = Field(alias="keyword", default=None)
    license: Optional[str] = Field(alias="license", default=None)
    media: Optional[List[Distribution]] = Field(alias="media", default=None)
    note: Optional[List[str]] = Field(alias="note", default=None)
    research_area: Optional[List[str]] = Field(alias="research_area", default=None)
    scientific_domain: Optional[List[str]] = Field(
        alias="scientific_domain", default=None
    )

    @validator("platform")
    def platform_max_length(cls, value):
        assert len(value) <= 64
        return value

    @validator("platform_identifier")
    def platform_identifier_max_length(cls, value):
        assert len(value) <= 256
        return value

    @validator("name")
    def name_max_length(cls, value):
        assert len(value) <= 256
        return value

    @validator("description")
    def description_max_length(cls, value):
        assert len(value) <= 1800
        return value

    @validator("same_as")
    def same_as_max_length(cls, value):
        assert len(value) <= 256
        return value

    @validator("version")
    def version_max_length(cls, value):
        assert len(value) <= 256
        return value

    @validator("pid")
    def pid_max_length(cls, value):
        assert len(value) <= 64
        return value

    @validator("experimental_workflow")
    def experimental_workflow_max_length(cls, value):
        assert len(value) <= 1800
        return value

    @validator("execution_settings")
    def execution_settings_max_length(cls, value):
        assert len(value) <= 1800
        return value

    @validator("reproducibility_explanation")
    def reproducibility_explanation_max_length(cls, value):
        assert len(value) <= 1800
        return value


ExperimentCreate.update_forward_refs()
