"""Setup connection to Postgres DB."""

import databases

from src.setting import Settings


def setup_pg_database_connection(settings: Settings) -> databases.Database:
    """Try to setup pg connection in Fastapi app."""
    return databases.Database(
        f"postgresql+asyncpg://{settings.db_user}:{settings.db_pass.get_secret_value()}@{settings.db_host}:{settings.db_port}/{settings.db_name}",
        min_size=settings.min_conn,
        max_size=settings.max_conn,
    )


async def connect_pg_database(_database_obj: databases.Database) -> None:
    """Connect to postgres."""
    if _database_obj.is_connected:
        return

    await _database_obj.connect()


async def disconnect_pg_database(_database_obj: databases.Database) -> None:
    if not _database_obj.is_connected:
        return

    await _database_obj.disconnect()
