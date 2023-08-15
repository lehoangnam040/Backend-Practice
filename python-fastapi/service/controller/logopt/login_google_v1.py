"""Login api v1 with username / password."""
from fastapi import APIRouter, Form, Request, Response
from typing_extensions import Annotated

from service.configs.exceptions import HttpServiceError
from service.configs.response import ErrorApiResponse, SingleApiResponse
from service.configs.setting import SETTINGS
from service.resources import TEMPLATES
from service.use_cases import auth_google_service
from service.use_cases.auth_google.business import AuthResponse
from service.use_cases.auth_google.errors import ErrorCode

router = APIRouter()


@router.get(
    "/login",
    responses={404: {"model": ErrorApiResponse}, 500: {"model": ErrorApiResponse}},
)
async def login_google_v1(
    request: Request,
) -> Response:
    return TEMPLATES.TemplateResponse(
        "google.html",
        {
            "request": request,
            "client_id": SETTINGS.google_settings.client_id,
            "login_uri": SETTINGS.google_settings.login_uri,
        },
    )


@router.post(
    "/auth",
    responses={404: {"model": ErrorApiResponse}, 500: {"model": ErrorApiResponse}},
)
async def auth_google_v1(
    credential: Annotated[str, Form()],
) -> SingleApiResponse[AuthResponse]:
    resp, err = await auth_google_service.logic(credential)
    if err is None:
        return SingleApiResponse(item=resp)

    if err.error == ErrorCode.VALIDATE_FAILED:
        raise HttpServiceError(status_code=404, error=err)
    if err.error == ErrorCode.TECHNICAL_ERROR:
        raise HttpServiceError(status_code=500, error=err)

    raise HttpServiceError(status_code=500, error=err)
