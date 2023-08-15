from service.configs.repository import SupportedDbType
from service.configs.setting import SETTINGS
from service.vendor.password import password_hasher

from . import auth_google, auth_username_password, product

SUPPORTED_DB_TYPE = SupportedDbType(SETTINGS.db_type)

auth_username_password_service = auth_username_password.compose(
    SUPPORTED_DB_TYPE,
    password_hasher,
)
auth_google_service = auth_google.compose(SETTINGS.google_settings.client_id)
search_product_service = product.compose(
    SUPPORTED_DB_TYPE,
)
