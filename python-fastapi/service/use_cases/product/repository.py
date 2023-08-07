from typing import Protocol, runtime_checkable

from .entity import Product


@runtime_checkable
class SearchProductRepository(Protocol):
    async def search_products_by_name(
        self: "SearchProductRepository",
        name: str,
        cursor_next: int,
    ) -> list[Product]:
        ...
