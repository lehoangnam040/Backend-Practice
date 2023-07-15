"""Login api v1 with username / password."""
from fastapi import APIRouter

from service.configs.errors import ServiceErrorCode
from service.configs.exceptions import HttpServiceException
from service.configs.response import ErrorApiResponse, SingleApiResponse
from service.services.login import (
    LoginV1RequestBody,
    LoginV1ResponseBody,
    login_v1_service,
)

router = APIRouter()


@router.post(
    "/v1/login",
    responses={404: {"model": ErrorApiResponse}, 500: {"model": ErrorApiResponse}},
)
async def login_v1(
    login_req_body: LoginV1RequestBody,
) -> SingleApiResponse[LoginV1ResponseBody]:
    """ """
    resp, err = await login_v1_service.login_by_username_password(login_req_body)
    if err is None:
        return SingleApiResponse(item=resp)

    if err.code == ServiceErrorCode.INCORRECT_USERNAME_PASSWORD:
        raise HttpServiceException(status_code=404, error=err)
    elif err.code == ServiceErrorCode.TECHNICAL_ERROR:
        raise HttpServiceException(status_code=500, error=err)
    else:
        raise HttpServiceException(status_code=500, error=err)
