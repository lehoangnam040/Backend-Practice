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
        rows = await self.database.fetch_one(
            query="SELECT * FROM account WHERE username = :username LIMIT 10",
            values={"username": username},
        )
        return Account.model_validate(rows, from_attributes=True)
