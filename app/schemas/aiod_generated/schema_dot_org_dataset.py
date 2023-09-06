# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

from app.schemas.aiod_generated.schema_dot_org_context import SchemaDotOrgContext


class SchemaDotOrgDataset(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SchemaDotOrgDataset - a model defined in OpenAPI

        context: The context of this SchemaDotOrgDataset [Optional].
        type: The type of this SchemaDotOrgDataset [Optional].
        name: The name of this SchemaDotOrgDataset.
        description: The description of this SchemaDotOrgDataset [Optional].
        identifier: The identifier of this SchemaDotOrgDataset.
        alternate_name: The alternate_name of this SchemaDotOrgDataset [Optional].
        citation: The citation of this SchemaDotOrgDataset [Optional].
        creator: The creator of this SchemaDotOrgDataset [Optional].
        date_modified: The date_modified of this SchemaDotOrgDataset [Optional].
        date_published: The date_published of this SchemaDotOrgDataset [Optional].
        is_accessible_for_free: The is_accessible_for_free of this SchemaDotOrgDataset [Optional].
        keywords: The keywords of this SchemaDotOrgDataset [Optional].
        same_as: The same_as of this SchemaDotOrgDataset [Optional].
        version: The version of this SchemaDotOrgDataset [Optional].
        url: The url of this SchemaDotOrgDataset [Optional].
        distribution: The distribution of this SchemaDotOrgDataset [Optional].
        funder: The funder of this SchemaDotOrgDataset [Optional].
        issn: The issn of this SchemaDotOrgDataset [Optional].
        license: The license of this SchemaDotOrgDataset [Optional].
        measurement_technique: The measurement_technique of this SchemaDotOrgDataset [Optional].
        size: The size of this SchemaDotOrgDataset [Optional].
        temporal_coverage: The temporal_coverage of this SchemaDotOrgDataset [Optional].
    """

    context: Optional[SchemaDotOrgContext] = Field(alias="@context", default=None)
    type: Optional[object] = Field(alias="@type", default=None)
    name: object = Field(alias="name")
    description: Optional[object] = Field(alias="description", default=None)
    identifier: object = Field(alias="identifier")
    alternate_name: Optional[object] = Field(alias="alternateName", default=None)
    citation: Optional[object] = Field(alias="citation", default=None)
    creator: Optional[object] = Field(alias="creator", default=None)
    date_modified: Optional[object] = Field(alias="dateModified", default=None)
    date_published: Optional[object] = Field(alias="datePublished", default=None)
    is_accessible_for_free: Optional[object] = Field(
        alias="isAccessibleForFree", default=None
    )
    keywords: Optional[object] = Field(alias="keywords", default=None)
    same_as: Optional[object] = Field(alias="sameAs", default=None)
    version: Optional[object] = Field(alias="version", default=None)
    url: Optional[object] = Field(alias="url", default=None)
    distribution: Optional[object] = Field(alias="distribution", default=None)
    funder: Optional[object] = Field(alias="funder", default=None)
    issn: Optional[object] = Field(alias="issn", default=None)
    license: Optional[object] = Field(alias="license", default=None)
    measurement_technique: Optional[object] = Field(
        alias="measurementTechnique", default=None
    )
    size: Optional[object] = Field(alias="size", default=None)
    temporal_coverage: Optional[object] = Field(alias="temporalCoverage", default=None)


SchemaDotOrgDataset.update_forward_refs()
