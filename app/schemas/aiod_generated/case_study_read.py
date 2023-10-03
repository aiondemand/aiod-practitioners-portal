# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

from app.schemas.aiod_generated.aio_d_entry_read import AIoDEntryRead
from app.schemas.aiod_generated.distribution import Distribution


class CaseStudyRead(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CaseStudyRead - a model defined in OpenAPI

        platform: The platform of this CaseStudyRead [Optional].
        platform_identifier: The platform_identifier of this CaseStudyRead [Optional].
        name: The name of this CaseStudyRead.
        description: The description of this CaseStudyRead [Optional].
        same_as: The same_as of this CaseStudyRead [Optional].
        date_published: The date_published of this CaseStudyRead [Optional].
        is_accessible_for_free: The is_accessible_for_free of this CaseStudyRead [Optional].
        version: The version of this CaseStudyRead [Optional].
        ai_asset_identifier: The ai_asset_identifier of this CaseStudyRead [Optional].
        ai_resource_identifier: The ai_resource_identifier of this CaseStudyRead [Optional].
        aiod_entry: The aiod_entry of this CaseStudyRead [Optional].
        alternate_name: The alternate_name of this CaseStudyRead [Optional].
        application_area: The application_area of this CaseStudyRead [Optional].
        citation: The citation of this CaseStudyRead [Optional].
        contact: The contact of this CaseStudyRead [Optional].
        creator: The creator of this CaseStudyRead [Optional].
        distribution: The distribution of this CaseStudyRead [Optional].
        has_part: The has_part of this CaseStudyRead [Optional].
        industrial_sector: The industrial_sector of this CaseStudyRead [Optional].
        is_part_of: The is_part_of of this CaseStudyRead [Optional].
        keyword: The keyword of this CaseStudyRead [Optional].
        license: The license of this CaseStudyRead [Optional].
        media: The media of this CaseStudyRead [Optional].
        note: The note of this CaseStudyRead [Optional].
        research_area: The research_area of this CaseStudyRead [Optional].
        scientific_domain: The scientific_domain of this CaseStudyRead [Optional].
        identifier: The identifier of this CaseStudyRead.
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
    ai_asset_identifier: Optional[int] = Field(
        alias="ai_asset_identifier", default=None
    )
    ai_resource_identifier: Optional[int] = Field(
        alias="ai_resource_identifier", default=None
    )
    aiod_entry: Optional[AIoDEntryRead] = Field(alias="aiod_entry", default=None)
    alternate_name: Optional[List[str]] = Field(alias="alternate_name", default=None)
    application_area: Optional[List[str]] = Field(
        alias="application_area", default=None
    )
    citation: Optional[List[int]] = Field(alias="citation", default=None)
    contact: Optional[List[int]] = Field(alias="contact", default=None)
    creator: Optional[List[int]] = Field(alias="creator", default=None)
    distribution: Optional[List[Distribution]] = Field(
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
    identifier: int = Field(alias="identifier")

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


CaseStudyRead.update_forward_refs()
