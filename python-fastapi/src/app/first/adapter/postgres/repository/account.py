import typing

from src.app.first.entity.account import Account

if typing.TYPE_CHECKING:
    from databases import Database


class Repository:

    def __init__(self, database: "Database") -> None:
        self.database = database

    async def get_an_account_by_username(
        self: "Repository",
        username: str,
    ) -> Account:
        return None
        # pg_account = (
        #     await PgAccount.objects.filter(username=username).limit(1).get_or_none()
        # )
        # assert pg_account is not None
        # return Account.validate(pg_account)
