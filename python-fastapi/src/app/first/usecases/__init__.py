from dataclasses import dataclass

from src.app.first.adapter.postgres.repository import PgRepositories
from src.setting import Settings
from src.vendor.bcrypt import BcryptPasslibPasswordHasher

from . import uc_auth_google, uc_login_usrname_pwd, uc_product_search


@dataclass
class Usecases:
    auth_username_password: uc_login_usrname_pwd.Usecase
    auth_google: uc_auth_google.Usecase
    search_product: uc_product_search.Usecase


def setup(settings: Settings, repositories: PgRepositories) -> Usecases:
    return Usecases(
        auth_google=uc_auth_google.Usecase(
            google_client_id=settings.google_settings.client_id,
        ),
        auth_username_password=uc_login_usrname_pwd.Usecase(
            account_repository=repositories.account,
            password_hasher=BcryptPasslibPasswordHasher(),
        ),
        search_product=uc_product_search.Usecase(
            repository=repositories.product,
        ),
    )
