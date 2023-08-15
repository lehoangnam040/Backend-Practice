"""Login api v1 with username / password."""
from fastapi import APIRouter

from service.configs.exceptions import HttpServiceError
from service.configs.response import ErrorApiResponse, SingleApiResponse
from service.use_cases import auth_username_password_service
from service.use_cases.auth_username_password.business import AuthRequest, AuthResponse
from service.use_cases.auth_username_password.errors import ErrorCode

router = APIRouter()


@router.post(
    "/v1/login",
    responses={404: {"model": ErrorApiResponse}, 500: {"model": ErrorApiResponse}},
)
async def login_v1(
    login_req_body: AuthRequest,
) -> SingleApiResponse[AuthResponse]:
    resp, err = await auth_username_password_service.logic(login_req_body)
    if err is None:
        return SingleApiResponse(item=resp)

    if err.error == ErrorCode.INCORRECT_USERNAME_PASSWORD:
        raise HttpServiceError(status_code=404, error=err)
    if err.error == ErrorCode.TECHNICAL_ERROR:
        raise HttpServiceError(status_code=500, error=err)

    raise HttpServiceError(status_code=500, error=err)
