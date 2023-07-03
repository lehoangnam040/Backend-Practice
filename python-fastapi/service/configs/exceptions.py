"""Logic handle when exception caused."""
from fastapi import FastAPI, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from service.configs.response import BaseApiResponse


async def http_exception_handler(_: Request, exc: HTTPException) -> JSONResponse:
    """Handle when `HTTPException` happened."""
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(BaseApiResponse(code="1", message=exc.detail)),
    )


def setup_exception_handlers(app: FastAPI) -> None:
    """Map all handle to corresponding exceptions."""
    app.add_exception_handler(HTTPException, http_exception_handler)
