# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

from app.schemas.aiod_generated.aio_d_entry_read import AIoDEntryRead


class ComputationalAssetRead(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ComputationalAssetRead - a model defined in OpenAPI

        platform: The platform of this ComputationalAssetRead [Optional].
        platform_identifier: The platform_identifier of this ComputationalAssetRead [Optional].
        name: The name of this ComputationalAssetRead.
        description: The description of this ComputationalAssetRead [Optional].
        same_as: The same_as of this ComputationalAssetRead [Optional].
        date_published: The date_published of this ComputationalAssetRead [Optional].
        is_accessible_for_free: The is_accessible_for_free of this ComputationalAssetRead [Optional].
        version: The version of this ComputationalAssetRead [Optional].
        status_info: The status_info of this ComputationalAssetRead [Optional].
        ai_asset_identifier: The ai_asset_identifier of this ComputationalAssetRead [Optional].
        ai_resource_identifier: The ai_resource_identifier of this ComputationalAssetRead [Optional].
        aiod_entry: The aiod_entry of this ComputationalAssetRead [Optional].
        alternate_name: The alternate_name of this ComputationalAssetRead [Optional].
        application_area: The application_area of this ComputationalAssetRead [Optional].
        citation: The citation of this ComputationalAssetRead [Optional].
        contact: The contact of this ComputationalAssetRead [Optional].
        creator: The creator of this ComputationalAssetRead [Optional].
        distribution: The distribution of this ComputationalAssetRead [Optional].
        has_part: The has_part of this ComputationalAssetRead [Optional].
        industrial_sector: The industrial_sector of this ComputationalAssetRead [Optional].
        is_part_of: The is_part_of of this ComputationalAssetRead [Optional].
        keyword: The keyword of this ComputationalAssetRead [Optional].
        license: The license of this ComputationalAssetRead [Optional].
        media: The media of this ComputationalAssetRead [Optional].
        note: The note of this ComputationalAssetRead [Optional].
        research_area: The research_area of this ComputationalAssetRead [Optional].
        scientific_domain: The scientific_domain of this ComputationalAssetRead [Optional].
        type: The type of this ComputationalAssetRead [Optional].
        identifier: The identifier of this ComputationalAssetRead.
    """

    platform: Optional[object] = Field(alias="platform", default=None)
    platform_identifier: Optional[object] = Field(
        alias="platform_identifier", default=None
    )
    name: object = Field(alias="name")
    description: Optional[object] = Field(alias="description", default=None)
    same_as: Optional[object] = Field(alias="same_as", default=None)
    date_published: Optional[object] = Field(alias="date_published", default=None)
    is_accessible_for_free: Optional[object] = Field(
        alias="is_accessible_for_free", default=None
    )
    version: Optional[object] = Field(alias="version", default=None)
    status_info: Optional[object] = Field(alias="status_info", default=None)
    ai_asset_identifier: Optional[object] = Field(
        alias="ai_asset_identifier", default=None
    )
    ai_resource_identifier: Optional[object] = Field(
        alias="ai_resource_identifier", default=None
    )
    aiod_entry: Optional[AIoDEntryRead] = Field(alias="aiod_entry", default=None)
    alternate_name: Optional[object] = Field(alias="alternate_name", default=None)
    application_area: Optional[object] = Field(alias="application_area", default=None)
    citation: Optional[object] = Field(alias="citation", default=None)
    contact: Optional[object] = Field(alias="contact", default=None)
    creator: Optional[object] = Field(alias="creator", default=None)
    distribution: Optional[object] = Field(alias="distribution", default=None)
    has_part: Optional[object] = Field(alias="has_part", default=None)
    industrial_sector: Optional[object] = Field(alias="industrial_sector", default=None)
    is_part_of: Optional[object] = Field(alias="is_part_of", default=None)
    keyword: Optional[object] = Field(alias="keyword", default=None)
    license: Optional[object] = Field(alias="license", default=None)
    media: Optional[object] = Field(alias="media", default=None)
    note: Optional[object] = Field(alias="note", default=None)
    research_area: Optional[object] = Field(alias="research_area", default=None)
    scientific_domain: Optional[object] = Field(alias="scientific_domain", default=None)
    type: Optional[object] = Field(alias="type", default=None)
    identifier: object = Field(alias="identifier")

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

    @validator("status_info")
    def status_info_max_length(cls, value):
        assert len(value) <= 256
        return value


ComputationalAssetRead.update_forward_refs()
