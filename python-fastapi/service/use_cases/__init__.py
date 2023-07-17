from service.configs.repository import SupportedDbType
from service.configs.setting import SETTINGS
from service.vendor.password import password_hasher

from . import auth_username_password

auth_username_password_service = auth_username_password.compose(
    SupportedDbType(SETTINGS.db_type),
    password_hasher,
)
