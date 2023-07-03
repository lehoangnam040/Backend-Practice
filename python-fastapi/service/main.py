"""Entrypoint of service."""
import logging

from fastapi import FastAPI

from service.configs.exceptions import setup_exception_handlers
from service.configs.setting import settings_factory
from service.controller.logopt import logopt_router
from service.repository.postgres import (
    connect_pg_database,
    disconnect_pg_database,
    setup_pg_database_connection,
)

settings = settings_factory()
logging.getLogger().setLevel(logging.INFO)
logging.info("App settings %s", settings)
app = FastAPI()

setup_exception_handlers(app)
setup_pg_database_connection(app)

app.include_router(logopt_router, prefix="/logopt")


@app.on_event("startup")
async def startup() -> None:
    """Run when starting service."""
    await connect_pg_database(app.state.database)


@app.on_event("shutdown")
async def shutdown() -> None:
    """Run when closing service."""
    await disconnect_pg_database(app.state.database)


@app.get("/")
async def main() -> str:
    """Home page of service."""
    return "Service"


@app.get("/health")
async def health() -> dict:
    """Return health status of service."""
    return {"status": "OK"}
