from fastapi import APIRouter

from .controller import (
    health,
)


def setup() -> APIRouter:

    router = APIRouter()

    router.include_router(health.router)
    return router
