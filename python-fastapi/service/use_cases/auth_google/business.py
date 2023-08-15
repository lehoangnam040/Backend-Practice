import sys
import typing

import cachecontrol
import requests
from google.auth.transport.requests import Request
from google.oauth2 import id_token

from service.configs.errors import (
    ServiceError,
    trace_debugs,
)
from service.configs.typing_compat import ResultWithErr

from .errors import DebugError, ErrorCode
from .validators import AuthResponse


class Business:
    def __init__(
        self: "Business",
        google_client_id: str,
    ) -> None:
        self.google_client_id = google_client_id
        session = requests.session()
        self.cached_session = cachecontrol.CacheControl(session)

    async def logic(
        self: "Business",
        credential: str,
    ) -> ResultWithErr[AuthResponse]:
        try:
            # sub, email, email_verified, picture, given_name, locale
            idinfo: dict[str, typing.Any] = id_token.verify_oauth2_token(
                credential, Request(session=self.cached_session), self.google_client_id
            )
        except Exception:
            linenos = trace_debugs(*sys.exc_info())
            return None, ServiceError(
                error=ErrorCode.VALIDATE_FAILED,
                debug_id=f"{DebugError.ERROR_VALIDATE_GOOGLE}:{linenos}",
            )

        return (
            AuthResponse(
                uid=idinfo["sub"],
                username=idinfo["email"],
            ),
            None,
        )
