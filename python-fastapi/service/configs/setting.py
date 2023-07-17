"""Global app settings."""

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


SETTINGS = Settings()
