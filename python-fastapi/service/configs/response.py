"""Structure/Definition of response in Api."""
from typing import Generic, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

DataType = TypeVar("DataType")


class ErrorApiResponse(BaseModel):
    code: str
    message: str
    debug_id: str


class SingleApiResponse(GenericModel, Generic[DataType]):

    """Api with response only 1 item."""

    item: DataType | None = None


class ListApiResponse(GenericModel, Generic[DataType]):

    """Api with response a list of items."""

    items: list[DataType] | None = None
