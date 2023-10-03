# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class AIoDEntryRead(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AIoDEntryRead - a model defined in OpenAPI

        editor: The editor of this AIoDEntryRead [Optional].
        status: The status of this AIoDEntryRead [Optional].
        date_modified: The date_modified of this AIoDEntryRead [Optional].
        date_created: The date_created of this AIoDEntryRead [Optional].
    """

    editor: Optional[List[int]] = Field(alias="editor", default=None)
    status: Optional[str] = Field(alias="status", default=None)
    date_modified: Optional[datetime] = Field(alias="date_modified", default=None)
    date_created: Optional[datetime] = Field(alias="date_created", default=None)


AIoDEntryRead.update_forward_refs()
