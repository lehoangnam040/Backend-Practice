"""Login api v1 with username / password."""

from fastapi import APIRouter

from src.app.first import global_var
from src.app.first.adapter.fastapi.exceptions import HttpServiceError
from src.app.first.adapter.fastapi.response import ErrorApiResponse, SingleApiResponse
from src.app.first.usecases import uc_login_usrname_pwd as uc
from src.app.first.usecases.errors import ErrorCode

router = APIRouter()


@router.post(
    "/v1/login",
    responses={404: {"model": ErrorApiResponse}, 500: {"model": ErrorApiResponse}},
)
async def login_v1(
    login_req_body: uc.Request,
) -> SingleApiResponse[uc.Response]:
    resp, err = await global_var().usecases.auth_username_password.logic(login_req_body)
    if err is None:
        return SingleApiResponse(item=resp)

    if err.error == ErrorCode.INCORRECT_USERNAME_PASSWORD:
        raise HttpServiceError(status_code=404, error=err)
    if err.error == ErrorCode.TECHNICAL_ERROR:
        raise HttpServiceError(status_code=500, error=err)

    raise HttpServiceError(status_code=500, error=err)
