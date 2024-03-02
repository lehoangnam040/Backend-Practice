"""Routers."""

import logging
import typing
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src import __version__
from src.app.first import usecases
from src.app.first.adapter.fastapi import exceptions, router
from src.app.first.adapter.postgres import repository as asyncpg_repository
from src.vendor import databases_asyncpg

from . import global_var

logging.getLogger().setLevel(logging.INFO)


@asynccontextmanager
async def lifespan(_app: FastAPI) -> typing.AsyncGenerator[None, None]:
    db_pg_instance = databases_asyncpg.setup_pg_database_connection(
        global_var().settings,
    )
    _app.state.db_pg_instance = db_pg_instance
    await databases_asyncpg.connect_pg_database(db_pg_instance)
    repositories = asyncpg_repository.setup(db_pg_instance)
    global_var().usecases = usecases.setup(global_var().settings, repositories)
    _app.include_router(router.setup())
    yield
    await databases_asyncpg.disconnect_pg_database(db_pg_instance)


app = FastAPI(version=__version__, lifespan=lifespan)
exceptions.setup(app)
