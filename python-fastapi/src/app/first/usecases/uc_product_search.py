from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from pydantic import BaseModel, TypeAdapter

from src.app.first.entity.product import Product
from src.error import ServiceError, trace_debugs

from .errors import DebugError, ErrorCode

if TYPE_CHECKING:
    from src.types import ResultWithErr


class Request(BaseModel):
    search: str
    cursor_next: int | None = 0


class Response(Product):
    pass


@runtime_checkable
class _Repository(Protocol):
    async def search_products_by_name(
        self,
        name: str,
        cursor_next: int | None,
    ) -> list[Product]: ...


class Usecase:
    def __init__(
        self,
        repository: _Repository,
    ) -> None:
        self.repository = repository

    async def logic(
        self,
        request: Request,
    ) -> ResultWithErr[list[Response]]:
        try:
            products = await self.repository.search_products_by_name(
                request.search,
                request.cursor_next,
            )
            return (
                TypeAdapter(list[Response]).validate_python(
                    products,
                    from_attributes=True,
                ),
                None,
            )
        except Exception:
            linenos = trace_debugs(*sys.exc_info())

            return None, ServiceError(
                error=ErrorCode.TECHNICAL_ERROR,
                debug_id=f"{DebugError.PYDANTIC_VALIDATE_FAILED}:{linenos}",
            )
