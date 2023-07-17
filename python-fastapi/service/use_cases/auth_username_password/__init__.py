from service.configs.repository import SupportedDbType
from service.vendor.password.interface import PasswordHasherInterface

from .business import Business
from .repository import AccountRepository


def _repository_factory(db_type: SupportedDbType) -> AccountRepository:
    if db_type == SupportedDbType.POSTGRES:
        from .repository_pg import PgAccountRepository

        return PgAccountRepository()
    raise NotImplementedError


def compose(
    db_type: SupportedDbType,
    password_hasher: PasswordHasherInterface,
) -> Business:
    return Business(_repository_factory(db_type), password_hasher)
