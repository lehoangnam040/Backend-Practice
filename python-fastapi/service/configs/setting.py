"""Global app settings."""
from functools import lru_cache

from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):

    """Global app settings."""

    # Database
    db_type: str = "postgres"
    db_host: str = "localhost"
    db_port: str = "5432"
    db_user: str = "postgres"
    db_pass: SecretStr = SecretStr("postgres")
    db_name: str = "service-db"

    class Config:

        """Config of settings."""

        env_prefix = "SERVICE_"


@lru_cache
def settings_factory() -> Settings:
    """Singleton of app's settings."""
    return Settings()
