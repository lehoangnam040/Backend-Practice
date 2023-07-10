from typing import Protocol, runtime_checkable

from service.models.account import Account
from service.configs.typing_compat import ResultWithErr


@runtime_checkable
class AccountRepository(Protocol):
    async def get_an_account_by_username(
        self: "AccountRepository",
        username: str,
    ) -> ResultWithErr[Account]:
        ...
