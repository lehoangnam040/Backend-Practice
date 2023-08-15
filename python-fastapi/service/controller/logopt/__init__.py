"""Module working with log... stuffs: Login / Logout / ..."""
from fastapi import APIRouter

from service.controller.logopt import login_google_v1, login_v1, password_v1

logopt_router = APIRouter()
logopt_router.include_router(login_v1.router)
logopt_router.include_router(password_v1.router)
logopt_router.include_router(login_google_v1.router)
