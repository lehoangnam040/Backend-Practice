from pydantic.errors import DictError

from service.models.account import Account

from .dao import PgAccount
from service.configs.typing_compat import ResultWithErr
from service.configs.errors import ServiceError, NOT_FOUND_ACCOUNT_IN_DB, PARSE_OBJECT_FAILED


class PgAccountRepository:
    async def get_an_account_by_username(
        self: "PgAccountRepository",
        username: str,
    ) -> ResultWithErr[Account]:
        pg_account = (
            await PgAccount.objects.filter(username=username).limit(1).get_or_none()
        )
        if not pg_account:
            return None, ServiceError(code=NOT_FOUND_ACCOUNT_IN_DB, detail=f"username={username} not found")
        try:
            return Account.validate(pg_account), None
        except (DictError, Exception) as err:
            return None, ServiceError(code=PARSE_OBJECT_FAILED, detail=f"parse object {pg_account} error {err}")
