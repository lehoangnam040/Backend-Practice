from fastapi import APIRouter

from .controller import (
    health,
    login_google_v1,
    login_username_password_v1,
    product_list_v1,
)


def setup() -> APIRouter:

    router = APIRouter()

    router.include_router(health.router)
    router.include_router(login_google_v1.router)
    router.include_router(login_username_password_v1.router)
    router.include_router(product_list_v1.router)
    return router
