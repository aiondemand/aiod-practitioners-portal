# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

from app.schemas.aiod_generated.aio_d_entry_create import AIoDEntryCreate


class PersonCreate(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PersonCreate - a model defined in OpenAPI

        platform: The platform of this PersonCreate [Optional].
        platform_identifier: The platform_identifier of this PersonCreate [Optional].
        name: The name of this PersonCreate.
        description: The description of this PersonCreate [Optional].
        same_as: The same_as of this PersonCreate [Optional].
        given_name: The given_name of this PersonCreate [Optional].
        surname: The surname of this PersonCreate [Optional].
        price_per_hour_euro: The price_per_hour_euro of this PersonCreate [Optional].
        wants_to_be_contacted: The wants_to_be_contacted of this PersonCreate [Optional].
        aiod_entry: The aiod_entry of this PersonCreate [Optional].
        alternate_name: The alternate_name of this PersonCreate [Optional].
        application_area: The application_area of this PersonCreate [Optional].
        contact: The contact of this PersonCreate [Optional].
        email: The email of this PersonCreate [Optional].
        expertise: The expertise of this PersonCreate [Optional].
        has_part: The has_part of this PersonCreate [Optional].
        industrial_sector: The industrial_sector of this PersonCreate [Optional].
        is_part_of: The is_part_of of this PersonCreate [Optional].
        keyword: The keyword of this PersonCreate [Optional].
        language: The language of this PersonCreate [Optional].
        media: The media of this PersonCreate [Optional].
        note: The note of this PersonCreate [Optional].
        research_area: The research_area of this PersonCreate [Optional].
        scientific_domain: The scientific_domain of this PersonCreate [Optional].
        telephone: The telephone of this PersonCreate [Optional].
    """

    platform: Optional[object] = Field(alias="platform", default=None)
    platform_identifier: Optional[object] = Field(
        alias="platform_identifier", default=None
    )
    name: object = Field(alias="name")
    description: Optional[object] = Field(alias="description", default=None)
    same_as: Optional[object] = Field(alias="same_as", default=None)
    given_name: Optional[object] = Field(alias="given_name", default=None)
    surname: Optional[object] = Field(alias="surname", default=None)
    price_per_hour_euro: Optional[object] = Field(
        alias="price_per_hour_euro", default=None
    )
    wants_to_be_contacted: Optional[object] = Field(
        alias="wants_to_be_contacted", default=None
    )
    aiod_entry: Optional[AIoDEntryCreate] = Field(alias="aiod_entry", default=None)
    alternate_name: Optional[object] = Field(alias="alternate_name", default=None)
    application_area: Optional[object] = Field(alias="application_area", default=None)
    contact: Optional[object] = Field(alias="contact", default=None)
    email: Optional[object] = Field(alias="email", default=None)
    expertise: Optional[object] = Field(alias="expertise", default=None)
    has_part: Optional[object] = Field(alias="has_part", default=None)
    industrial_sector: Optional[object] = Field(alias="industrial_sector", default=None)
    is_part_of: Optional[object] = Field(alias="is_part_of", default=None)
    keyword: Optional[object] = Field(alias="keyword", default=None)
    language: Optional[object] = Field(alias="language", default=None)
    media: Optional[object] = Field(alias="media", default=None)
    note: Optional[object] = Field(alias="note", default=None)
    research_area: Optional[object] = Field(alias="research_area", default=None)
    scientific_domain: Optional[object] = Field(alias="scientific_domain", default=None)
    telephone: Optional[object] = Field(alias="telephone", default=None)

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

    @validator("given_name")
    def given_name_max_length(cls, value):
        assert len(value) <= 256
        return value

    @validator("surname")
    def surname_max_length(cls, value):
        assert len(value) <= 256
        return value


PersonCreate.update_forward_refs()
