"""Logic handle when exception caused."""

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.app.first.usecases.errors import ServiceError

from .response import ErrorApiResponse


class HttpServiceError(RuntimeError):
    def __init__(
        self: "HttpServiceError",
        *args: object,
        status_code: int,
        error: ServiceError,
    ) -> None:
        super().__init__(*args)
        self.status_code = status_code
        self.error = error


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


def setup_exception_handlers(app: FastAPI) -> None:
    """Map all handle to corresponding exceptions."""
    app.add_exception_handler(HttpServiceError, http_exception_handler)
