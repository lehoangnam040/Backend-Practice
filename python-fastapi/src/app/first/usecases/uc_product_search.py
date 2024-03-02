from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from pydantic import BaseModel, parse_obj_as

from .errors import DebugError, ErrorCode, ResultWithErr, ServiceError, trace_debugs

if TYPE_CHECKING:
    from src.app.first.entity.product import Product


class Request(BaseModel):
    search: str
    cursor_next: int | None = 0


class Response(BaseModel):
    pid: int
    product_name: str
    description: str


@runtime_checkable
class _Repository(Protocol):
    async def search_products_by_name(
        self: _Repository,
        name: str,
        cursor_next: int | None,
    ) -> list[Product]: ...


class Usecase:
    def __init__(
        self: Usecase,
        repository: _Repository,
    ) -> None:
        self.repository = repository

    async def logic(
        self: Usecase,
        request: Request,
    ) -> ResultWithErr[list[Response]]:
        try:
            products = await self.repository.search_products_by_name(
                request.search,
                request.cursor_next,
            )
            return parse_obj_as(list[Response], products), None
        except Exception:
            linenos = trace_debugs(*sys.exc_info())
            return None, ServiceError(
                error=ErrorCode.TECHNICAL_ERROR,
                debug_id=f"{DebugError.PYDANTIC_VALIDATE_FAILED}:{linenos}",
            )
