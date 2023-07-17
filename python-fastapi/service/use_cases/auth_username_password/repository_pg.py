from service.databases.postgres.account import PgAccount

from .entity import Account


class PgAccountRepository:
    async def get_an_account_by_username(
        self: "PgAccountRepository",
        username: str,
    ) -> Account:
        pg_account = (
            await PgAccount.objects.filter(username=username).limit(1).get_or_none()
        )
        assert pg_account is not None
        return Account.validate(pg_account)
