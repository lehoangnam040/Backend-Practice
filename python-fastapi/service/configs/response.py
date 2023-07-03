"""Structure/Definition of response in Api."""
from typing import Generic, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

DataType = TypeVar("DataType")


class BaseApiResponse(BaseModel):

    """Basic response of every api."""

    code: str
    message: str


class SingleApiResponse(BaseApiResponse, GenericModel, Generic[DataType]):

    """Api with response only 1 item."""

    item: DataType | None = None


class ListApiResponse(BaseApiResponse, GenericModel, Generic[DataType]):

    """Api with response a list of items."""

    items: list[DataType] | None = None
