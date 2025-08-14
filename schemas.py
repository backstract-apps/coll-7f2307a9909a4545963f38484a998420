from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Profiles(BaseModel):
    id: int
    name: str
    contact: str


class ReadProfiles(BaseModel):
    id: int
    name: str
    contact: str
    class Config:
        from_attributes = True




class PostProfiles(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)
    contact: str = Field(..., max_length=100)

    class Config:
        from_attributes = True

