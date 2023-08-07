"""Module working with log... stuffs: Login / Logout / ..."""
from fastapi import APIRouter

from . import list_v1

product_router = APIRouter()
product_router.include_router(list_v1.router)
