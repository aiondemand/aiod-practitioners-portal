# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

from app.schemas.aiod_generated.aio_d_entry_create import AIoDEntryCreate


class ProjectCreate(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ProjectCreate - a model defined in OpenAPI

        platform: The platform of this ProjectCreate [Optional].
        platform_identifier: The platform_identifier of this ProjectCreate [Optional].
        name: The name of this ProjectCreate.
        description: The description of this ProjectCreate [Optional].
        same_as: The same_as of this ProjectCreate [Optional].
        start_date: The start_date of this ProjectCreate [Optional].
        end_date: The end_date of this ProjectCreate [Optional].
        total_cost_euro: The total_cost_euro of this ProjectCreate [Optional].
        aiod_entry: The aiod_entry of this ProjectCreate [Optional].
        alternate_name: The alternate_name of this ProjectCreate [Optional].
        application_area: The application_area of this ProjectCreate [Optional].
        contact: The contact of this ProjectCreate [Optional].
        coordinator: The coordinator of this ProjectCreate [Optional].
        funder: The funder of this ProjectCreate [Optional].
        has_part: The has_part of this ProjectCreate [Optional].
        industrial_sector: The industrial_sector of this ProjectCreate [Optional].
        is_part_of: The is_part_of of this ProjectCreate [Optional].
        keyword: The keyword of this ProjectCreate [Optional].
        media: The media of this ProjectCreate [Optional].
        note: The note of this ProjectCreate [Optional].
        participant: The participant of this ProjectCreate [Optional].
        produced: The produced of this ProjectCreate [Optional].
        research_area: The research_area of this ProjectCreate [Optional].
        scientific_domain: The scientific_domain of this ProjectCreate [Optional].
        used: The used of this ProjectCreate [Optional].
    """

    platform: Optional[object] = Field(alias="platform", default=None)
    platform_identifier: Optional[object] = Field(
        alias="platform_identifier", default=None
    )
    name: object = Field(alias="name")
    description: Optional[object] = Field(alias="description", default=None)
    same_as: Optional[object] = Field(alias="same_as", default=None)
    start_date: Optional[object] = Field(alias="start_date", default=None)
    end_date: Optional[object] = Field(alias="end_date", default=None)
    total_cost_euro: Optional[object] = Field(alias="total_cost_euro", default=None)
    aiod_entry: Optional[AIoDEntryCreate] = Field(alias="aiod_entry", default=None)
    alternate_name: Optional[object] = Field(alias="alternate_name", default=None)
    application_area: Optional[object] = Field(alias="application_area", default=None)
    contact: Optional[object] = Field(alias="contact", default=None)
    coordinator: Optional[object] = Field(alias="coordinator", default=None)
    funder: Optional[object] = Field(alias="funder", default=None)
    has_part: Optional[object] = Field(alias="has_part", default=None)
    industrial_sector: Optional[object] = Field(alias="industrial_sector", default=None)
    is_part_of: Optional[object] = Field(alias="is_part_of", default=None)
    keyword: Optional[object] = Field(alias="keyword", default=None)
    media: Optional[object] = Field(alias="media", default=None)
    note: Optional[object] = Field(alias="note", default=None)
    participant: Optional[object] = Field(alias="participant", default=None)
    produced: Optional[object] = Field(alias="produced", default=None)
    research_area: Optional[object] = Field(alias="research_area", default=None)
    scientific_domain: Optional[object] = Field(alias="scientific_domain", default=None)
    used: Optional[object] = Field(alias="used", default=None)

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


ProjectCreate.update_forward_refs()
