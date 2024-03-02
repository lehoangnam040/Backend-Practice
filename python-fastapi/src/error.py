from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from enum import Enum
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


class HttpServiceError(RuntimeError):
    def __init__(
        self,
        *args: object,
        status_code: int,
        error: ServiceError,
    ) -> None:
        super().__init__(*args)
        self.status_code = status_code
        self.error = error
