from __future__ import annotations

from enum import Enum, StrEnum
from typing import TYPE_CHECKING, TypeVar

from pydantic import BaseModel

if TYPE_CHECKING:
    from types import TracebackType


def trace_debugs(
    _: type[BaseException] | None,
    __: BaseException | None,
    tb: TracebackType | None,
) -> str:
    linenos = []
    while tb:
        linenos.append(tb.tb_lineno)
        tb = tb.tb_next
    return ".".join(map(str, linenos))


class ServiceError(BaseModel):
    error: Enum
    debug_id: str


class ErrorCode(Enum):
    VALIDATE_FAILED = "Validate failed with google"
    INCORRECT_USERNAME_PASSWORD = "Incorrect username or password"
    TECHNICAL_ERROR = "Oops, something went wrong. Please try again later"


class DebugError(StrEnum):
    # repository
    NOT_FOUND_ON_DB = "R1001"

    # vendor
    PYDANTIC_VALIDATE_FAILED = "V1001"
    PASSWORD_VERIFY_FAILED = "V1002"
    ERROR_VALIDATE_GOOGLE = "V1003"


T = TypeVar("T")
ResultWithErr = tuple[T | None, ServiceError | None]
EnumerationT = TypeVar("EnumerationT", bound=type[Enum])
