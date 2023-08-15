import typing
from enum import Enum
from types import TracebackType

from pydantic import BaseModel

if typing.TYPE_CHECKING:
    from .typing_compat import EnumerationT


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


error_codes = set()


def service_error_enum_unique(enumeration: "EnumerationT") -> "EnumerationT":
    for name, member in enumeration.__members__.items():
        if member.name in error_codes:
            msg = f"duplicate values found in {enumeration!r}: {name}"
            raise ValueError(msg)
        error_codes.add(member.name)
    return enumeration


debug_errors = set()


def debug_error_enum_unique(enumeration: "EnumerationT") -> "EnumerationT":
    for name, member in enumeration.__members__.items():
        if member.value in debug_errors:
            msg = f"duplicate values found in {enumeration!r}: {name}"
            raise ValueError(msg)
        debug_errors.add(member.name)
    return enumeration
