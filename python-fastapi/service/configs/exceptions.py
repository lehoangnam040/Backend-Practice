"""Logic handle when exception caused."""
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from service.configs.response import ErrorApiResponse

from .errors import ServiceError


class HttpServiceException(RuntimeError):
    def __init__(self, *args: object, status_code: int, error: ServiceError) -> None:
        super().__init__(*args)
        self.status_code = status_code
        self.error = error


async def http_exception_handler(_: Request, exc: HttpServiceException) -> JSONResponse:
    """Handle when `HTTPException` happened."""
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(
            ErrorApiResponse(
                code=exc.error.code.name,
                message=exc.error.code.value,
                debug_id=exc.error.debug_id,
            ),
        ),
    )


def setup_exception_handlers(app: FastAPI) -> None:
    """Map all handle to corresponding exceptions."""
    app.add_exception_handler(HttpServiceException, http_exception_handler)
