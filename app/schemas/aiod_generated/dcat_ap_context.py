# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class DcatAPContext(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DcatAPContext - a model defined in OpenAPI

        dcat: The dcat of this DcatAPContext [Optional].
        dct: The dct of this DcatAPContext [Optional].
        vcard: The vcard of this DcatAPContext [Optional].
    """

    dcat: Optional[str] = Field(alias="dcat", default=None)
    dct: Optional[str] = Field(alias="dct", default=None)
    vcard: Optional[str] = Field(alias="vcard", default=None)


DcatAPContext.update_forward_refs()
