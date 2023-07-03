"""Setup connection to Postgres DB."""
import typing

import databases
import sqlalchemy
from fastapi import FastAPI

from service.configs.setting import settings_factory

settings = settings_factory()
DB_URL = f"postgresql://{settings.db_user}:{settings.db_pass.get_secret_value()}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
metadata = sqlalchemy.MetaData()
database = databases.Database(DB_URL)


def setup_pg_database_connection(app: FastAPI) -> None:
    """Try to setup pg connection in Fastapi app."""
    app.state.database = database


async def connect_pg_database(_database_obj: databases.Database | typing.Any) -> bool:
    """Connect to postgres."""
    if not isinstance(_database_obj, databases.Database):
        return False

    if _database_obj.is_connected:
        return False

    await _database_obj.connect()
    return True


async def disconnect_pg_database(
    _database_obj: databases.Database | typing.Any,
) -> bool:
    """Disconnect to postgres."""
    if not isinstance(_database_obj, databases.Database):
        return False

    if not _database_obj.is_connected:
        return False

    await _database_obj.disconnect()
    return True
