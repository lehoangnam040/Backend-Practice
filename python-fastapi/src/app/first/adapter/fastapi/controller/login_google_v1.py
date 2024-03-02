"""Login api v1 with username / password."""

from fastapi import APIRouter, Form, Request, Response
from typing_extensions import Annotated

from src.app.first import global_var
from src.app.first.adapter.fastapi.exceptions import HttpServiceError
from src.app.first.adapter.fastapi.response import ErrorApiResponse, SingleApiResponse
from src.app.first.usecases import uc_auth_google as uc
from src.app.first.usecases.errors import ErrorCode

router = APIRouter()


@router.get(
    "/login",
    responses={404: {"model": ErrorApiResponse}, 500: {"model": ErrorApiResponse}},
)
async def login_google_v1(request: Request) -> Response:
    return global_var().templates.TemplateResponse(
        "google.html",
        {
            "request": request,
            "client_id": global_var().settings.google_settings.client_id,
            "login_uri": global_var().settings.google_settings.login_uri,
        },
    )


@router.post(
    "/auth",
    responses={404: {"model": ErrorApiResponse}, 500: {"model": ErrorApiResponse}},
)
async def auth_google_v1(
    credential: Annotated[str, Form()],
) -> SingleApiResponse[uc.Response]:
    resp, err = await global_var().usecases.auth_google.logic(credential)
    if err is None:
        return SingleApiResponse(item=resp)

    if err.error == ErrorCode.VALIDATE_FAILED:
        raise HttpServiceError(status_code=404, error=err)
    if err.error == ErrorCode.TECHNICAL_ERROR:
        raise HttpServiceError(status_code=500, error=err)

    raise HttpServiceError(status_code=500, error=err)
