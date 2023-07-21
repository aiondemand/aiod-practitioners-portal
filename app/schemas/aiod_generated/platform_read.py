# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class PlatformRead(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PlatformRead - a model defined in OpenAPI

        name: The name of this PlatformRead.
        identifier: The identifier of this PlatformRead.
    """

    name: str = Field(alias="name")
    identifier: int = Field(alias="identifier")


PlatformRead.update_forward_refs()