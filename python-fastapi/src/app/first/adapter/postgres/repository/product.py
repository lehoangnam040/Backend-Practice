from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from databases import Database

    from src.app.first.entity.product import Product


class Repository:

    def __init__(self, database: Database) -> None:
        self.database = database

    async def search_products_by_name(
        self: Repository,
        name: str,
        cursor_next: int | None,
    ) -> list[Product]:
        return []
        # query = (
        #     PgProduct.objects.filter(
        #         product_name__icontains=name,
        #     )
        #     .order_by(PgProduct.pid.desc())
        #     .limit(10)
        # )
        # if not cursor_next:
        #     pg_products = await query.all()
        # else:
        #     pg_products = await query.filter(pid__lt=cursor_next).all()
        # return parse_obj_as(list[Product], pg_products)
