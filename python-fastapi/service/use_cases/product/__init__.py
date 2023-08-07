
from service.configs.repository import SupportedDbType

from .business.search_product import SearchProduct
from .repository import SearchProductRepository


def _repository_factory(db_type: SupportedDbType) -> SearchProductRepository:
    if db_type == SupportedDbType.POSTGRES:
        from .repository_pg import PgProductRepository

        return PgProductRepository()
    raise NotImplementedError


def compose(
    db_type: SupportedDbType,
) -> SearchProduct:
    return SearchProduct(_repository_factory(db_type))
