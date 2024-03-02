from __future__ import annotations

import typing

from src.app.first.entity.product import ListProduct, Product

if typing.TYPE_CHECKING:
    from databases import Database


class Repository:

    def __init__(self, database: Database) -> None:
        self.database = database

    async def search_products_by_name(
        self,
        name: str,
        cursor_next: int | None,
    ) -> list[Product]:
        values: dict[str, typing.Any]
        if not cursor_next:
            query = "SELECT * FROM product WHERE product_name ILIKE ('%' || :name || '%') ORDER BY pid DESC LIMIT 10"
            values = {"name": name}
        else:
            query = "SELECT * FROM product WHERE pid < :cursor_next AND product_name ILIKE ('%' || :name || '%') ORDER BY pid DESC LIMIT 10"
            values = {"name": name, "cursor_next": cursor_next}

        rows = await self.database.fetch_all(query=query, values=values)
        return ListProduct.validate_python(rows, from_attributes=True)
