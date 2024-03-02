import typing
from dataclasses import dataclass

from src.app.first.adapter.postgres.repository import account, product

if typing.TYPE_CHECKING:
    from databases import Database


@dataclass
class PgRepositories:
    account: account.Repository
    product: product.Repository


def setup(database: "Database") -> PgRepositories:
    return PgRepositories(
        account=account.Repository(database),
        product=product.Repository(database),
    )
