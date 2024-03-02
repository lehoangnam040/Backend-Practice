"""Logic handle when exception caused."""

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.error import HttpServiceError

from .response import ErrorApiResponse


async def http_exception_handler(_: Request, exc: HttpServiceError) -> JSONResponse:
    """Handle when `HTTPException` happened."""
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(
            ErrorApiResponse(
                code=exc.error.error.name,
                message=exc.error.error.value,
                debug_id=exc.error.debug_id,
            ),
        ),
    )


def setup(app: FastAPI) -> None:
    app.add_exception_handler(HttpServiceError, http_exception_handler)  # type: ignore
