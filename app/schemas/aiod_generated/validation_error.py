# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class ValidationError(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ValidationError - a model defined in OpenAPI

        loc: The loc of this ValidationError.
        msg: The msg of this ValidationError.
        type: The type of this ValidationError.
    """

    loc: object = Field(alias="loc")
    msg: object = Field(alias="msg")
    type: object = Field(alias="type")


ValidationError.update_forward_refs()
