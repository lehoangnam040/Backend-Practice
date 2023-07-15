"""Factory to create repository instances."""
from enum import Enum

from .account import AccountRepository


class SupportedDbType(Enum):
    POSTGRES = "postgres"


class RepositoryFactory:

    """Factory to create repository instances."""

    def __init__(self: "RepositoryFactory", db_type: SupportedDbType) -> None:
        """Init factory."""
        self.db_type = db_type

    def create_account_repository(self: "RepositoryFactory") -> AccountRepository:
        if self.db_type == SupportedDbType.POSTGRES:
            from service.repository.postgres.account.repository import (
                PgAccountRepository,
            )

            return PgAccountRepository()
        raise NotImplementedError
