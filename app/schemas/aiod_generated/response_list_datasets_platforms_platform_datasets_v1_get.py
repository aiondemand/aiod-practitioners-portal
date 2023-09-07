# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

from app.schemas.aiod_generated.dataset_read import DatasetRead
from app.schemas.aiod_generated.dcat_ap_wrapper import DcatApWrapper
from app.schemas.aiod_generated.schema_dot_org_dataset import SchemaDotOrgDataset


class ResponseListDatasetsPlatformsPlatformDatasetsV1Get(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ResponseListDatasetsPlatformsPlatformDatasetsV1Get - a model defined in OpenAPI

    """


ResponseListDatasetsPlatformsPlatformDatasetsV1Get.update_forward_refs()
