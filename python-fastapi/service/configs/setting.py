"""Global app settings."""

from pydantic import BaseSettings, SecretStr


class GoogleSettings(BaseSettings):

    client_id: str = "..."
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

    google_settings = GoogleSettings()

    class Config:

        """Config of settings."""

        env_prefix = "SERVICE_"



SETTINGS = Settings()
