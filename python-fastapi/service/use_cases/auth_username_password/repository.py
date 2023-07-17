from typing import Protocol, runtime_checkable

from .entity import Account


@runtime_checkable
class AccountRepository(Protocol):
    async def get_an_account_by_username(
        self: "AccountRepository",
        username: str,
    ) -> Account:
        """Get account from database by unique username. If any reason causes multiple username, return first result."""
        ...
