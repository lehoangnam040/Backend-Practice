"""Global app settings."""

from enum import Enum

from pydantic import SecretStr
from pydantic_settings import BaseSettings


class SupportedDbType(Enum):
    POSTGRES = "postgres"


class GoogleSettings(BaseSettings):
    client_id: str = (
        "303190471317-1ijeapcb36opb6cepsmatkouconf5i3q.apps.googleusercontent.com"
    )
    login_uri: str = "http://localhost:8000/auth"

    class Config:
        """Config of settings."""

        env_prefix = "GOOGLE_"


class Settings(BaseSettings):
    """Global app settings."""

    # Database
    db_type: str = "postgres"
    db_host: str = "localhost"
    db_port: str = "5432"
    db_user: str = "postgres"
    db_pass: SecretStr = SecretStr("postgres")
    db_name: str = "service-db"
    min_conn: int = 1
    max_conn: int = 10

    google_settings: GoogleSettings = GoogleSettings()

    class Config:
        """Config of settings."""

        env_prefix = "SERVICE_"
