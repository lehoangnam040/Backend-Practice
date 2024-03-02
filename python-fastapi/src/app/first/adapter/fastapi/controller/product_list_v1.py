"""Login api v1 with username / password."""

from fastapi import APIRouter, Depends

from src.app.first import global_var
from src.app.first.adapter.fastapi.exceptions import HttpServiceError
from src.app.first.adapter.fastapi.response import ErrorApiResponse, ListApiResponse
from src.app.first.usecases import uc_product_search as uc
from src.app.first.usecases.errors import ErrorCode

router = APIRouter()


@router.get(
    "/v1/products",
    responses={500: {"model": ErrorApiResponse}},
)
async def search_product_v1(
    search_params: uc.Request = Depends(),
) -> ListApiResponse[uc.Response]:
    resp, err = await global_var().usecases.search_product.logic(search_params)
    if err is None:
        return ListApiResponse(items=resp)

    if err.error == ErrorCode.TECHNICAL_ERROR:
        raise HttpServiceError(status_code=500, error=err)

    raise HttpServiceError(status_code=500, error=err)
