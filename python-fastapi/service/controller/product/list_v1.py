"""Login api v1 with username / password."""
from fastapi import APIRouter, Depends

from service.configs.exceptions import HttpServiceException
from service.configs.response import ErrorApiResponse, ListApiResponse
from service.use_cases import search_product_service
from service.use_cases.product.business.search_product import (
    SearchProductRequest,
    SearchProductResponse,
)
from service.use_cases.product.errors import ErrorCode

router = APIRouter()


@router.get(
    "/v1/products",
    responses={500: {"model": ErrorApiResponse}},
)
async def search_product_v1(
    search_params: SearchProductRequest = Depends(),
) -> ListApiResponse[SearchProductResponse]:
    """ """
    resp, err = await search_product_service.logic(search_params)
    if err is None:
        return ListApiResponse(items=resp)

    if err.error == ErrorCode.TECHNICAL_ERROR:
        raise HttpServiceException(status_code=500, error=err)
    else:
        raise HttpServiceException(status_code=500, error=err)
