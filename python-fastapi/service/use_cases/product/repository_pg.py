
from pydantic import parse_obj_as

from service.databases.postgres.product import PgProduct

from .entity import Product


class PgProductRepository:
    async def search_products_by_name(
        self: "PgProductRepository",
        name: str,
        cursor_next: int,
    ) -> list[Product]:
        query = PgProduct.objects.filter(
            product_name__icontains=name,
        ).order_by(PgProduct.pid.desc()).limit(10)
        if not cursor_next:
            pg_products = await query.all()
        else:
            pg_products = await query.filter(pid__lt=cursor_next).all()
        return parse_obj_as(list[Product], pg_products)
