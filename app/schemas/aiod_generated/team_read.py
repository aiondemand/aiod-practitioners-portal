# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

from app.schemas.aiod_generated.aio_d_entry_read import AIoDEntryRead


class TeamRead(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TeamRead - a model defined in OpenAPI

        platform: The platform of this TeamRead [Optional].
        platform_identifier: The platform_identifier of this TeamRead [Optional].
        name: The name of this TeamRead.
        description: The description of this TeamRead [Optional].
        same_as: The same_as of this TeamRead [Optional].
        price_per_hour_euro: The price_per_hour_euro of this TeamRead [Optional].
        size: The size of this TeamRead [Optional].
        ai_resource_identifier: The ai_resource_identifier of this TeamRead [Optional].
        aiod_entry: The aiod_entry of this TeamRead [Optional].
        alternate_name: The alternate_name of this TeamRead [Optional].
        application_area: The application_area of this TeamRead [Optional].
        contact: The contact of this TeamRead [Optional].
        has_part: The has_part of this TeamRead [Optional].
        industrial_sector: The industrial_sector of this TeamRead [Optional].
        is_part_of: The is_part_of of this TeamRead [Optional].
        keyword: The keyword of this TeamRead [Optional].
        media: The media of this TeamRead [Optional].
        member: The member of this TeamRead [Optional].
        note: The note of this TeamRead [Optional].
        organisation: The organisation of this TeamRead [Optional].
        research_area: The research_area of this TeamRead [Optional].
        scientific_domain: The scientific_domain of this TeamRead [Optional].
        identifier: The identifier of this TeamRead.
    """

    platform: Optional[object] = Field(alias="platform", default=None)
    platform_identifier: Optional[object] = Field(
        alias="platform_identifier", default=None
    )
    name: object = Field(alias="name")
    description: Optional[object] = Field(alias="description", default=None)
    same_as: Optional[object] = Field(alias="same_as", default=None)
    price_per_hour_euro: Optional[object] = Field(
        alias="price_per_hour_euro", default=None
    )
    size: Optional[object] = Field(alias="size", default=None)
    ai_resource_identifier: Optional[object] = Field(
        alias="ai_resource_identifier", default=None
    )
    aiod_entry: Optional[AIoDEntryRead] = Field(alias="aiod_entry", default=None)
    alternate_name: Optional[object] = Field(alias="alternate_name", default=None)
    application_area: Optional[object] = Field(alias="application_area", default=None)
    contact: Optional[object] = Field(alias="contact", default=None)
    has_part: Optional[object] = Field(alias="has_part", default=None)
    industrial_sector: Optional[object] = Field(alias="industrial_sector", default=None)
    is_part_of: Optional[object] = Field(alias="is_part_of", default=None)
    keyword: Optional[object] = Field(alias="keyword", default=None)
    media: Optional[object] = Field(alias="media", default=None)
    member: Optional[object] = Field(alias="member", default=None)
    note: Optional[object] = Field(alias="note", default=None)
    organisation: Optional[object] = Field(alias="organisation", default=None)
    research_area: Optional[object] = Field(alias="research_area", default=None)
    scientific_domain: Optional[object] = Field(alias="scientific_domain", default=None)
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


TeamRead.update_forward_refs()
