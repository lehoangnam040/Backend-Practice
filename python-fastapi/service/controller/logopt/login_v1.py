"""Login api v1 with username / password."""
from fastapi import APIRouter, HTTPException

from service.configs.response import BaseApiResponse, SingleApiResponse
from service.services.login import (
    LoginV1RequestBody,
    LoginV1ResponseBody,
    login_v1_service,
)

router = APIRouter()


@router.post(
    "/v1/login",
    responses={404: {"model": BaseApiResponse}, 500: {"model": BaseApiResponse}},
)
async def login_v1(
    login_req_body: LoginV1RequestBody,
) -> SingleApiResponse[LoginV1ResponseBody]:
    """ """
    err, resp = await login_v1_service.login_by_username_password(login_req_body)
    if err is not None:
        raise HTTPException(status_code=404, detail=str(err))

    return SingleApiResponse(code="", message="OK", item=resp)
