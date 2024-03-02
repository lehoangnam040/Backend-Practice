"""Structure/Definition of response in Api."""

from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

DataType = TypeVar("DataType")


class ErrorApiResponse(BaseModel):
    code: str
    message: str
    debug_id: str


class SingleApiResponse(GenericModel, Generic[DataType]):

    item: DataType | None = None


class ListApiResponse(GenericModel, Generic[DataType]):

    items: list[DataType] | None = None
