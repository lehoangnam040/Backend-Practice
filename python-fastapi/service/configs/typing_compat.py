from enum import Enum
from typing import TypeVar

from .errors import ServiceError

T = TypeVar("T")
ResultWithErr = tuple[T | None, ServiceError | None]
EnumerationT = TypeVar("EnumerationT", bound=type[Enum])
