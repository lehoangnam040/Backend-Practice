import sys

from pydantic import parse_obj_as

from service.configs.errors import (
    ServiceError,
    trace_debugs,
)
from service.configs.typing_compat import ResultWithErr
from service.use_cases.product.errors import DebugError, ErrorCode
from service.use_cases.product.repository import SearchProductRepository
from service.use_cases.product.validators import (
    SearchProductRequest,
    SearchProductResponse,
)


class SearchProduct:
    def __init__(
        self: "SearchProduct",
        repository: SearchProductRepository,
    ) -> None:
        self.repository = repository

    async def logic(
        self: "SearchProduct",
        request: SearchProductRequest,
    ) -> ResultWithErr[list[SearchProductResponse]]:
        try:
            products = await self.repository.search_products_by_name(request.search, request.cursor_next)
            return parse_obj_as(list[SearchProductResponse], products), None
        except Exception:
            linenos = trace_debugs(*sys.exc_info())
            return None, ServiceError(
                error=ErrorCode.TECHNICAL_ERROR,
                debug_id=f"{DebugError.PYDANTIC_VALIDATE_FAILED}:{linenos}",
            )
