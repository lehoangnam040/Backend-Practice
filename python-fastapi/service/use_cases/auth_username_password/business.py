import sys

from service.configs.errors import (
    ServiceError,
    trace_debugs,
)
from service.configs.typing_compat import ResultWithErr
from service.vendor.password.interface import PasswordHasherInterface

from .errors import DebugError, ErrorCode
from .repository import AccountRepository
from .validators import AuthRequest, AuthResponse


class Business:
    def __init__(
        self: "Business",
        account_repository: AccountRepository,
        password_hasher: PasswordHasherInterface,
    ) -> None:
        self.account_repository = account_repository
        self.password_hasher = password_hasher

    async def logic(
        self: "Business",
        request: AuthRequest,
    ) -> ResultWithErr[AuthResponse]:
        try:
            account = await self.account_repository.get_an_account_by_username(
                request.username,
            )
        except Exception:
            linenos = trace_debugs(*sys.exc_info())
            return None, ServiceError(
                error=ErrorCode.INCORRECT_USERNAME_PASSWORD,
                debug_id=f"{DebugError.NOT_FOUND_ON_DB}:{linenos}",
            )

        try:
            success = self.password_hasher.verify_hashed_password(
                request.password,
                account.hashed_password,
            )
            assert success is True
        except Exception:
            linenos = trace_debugs(*sys.exc_info())
            return None, ServiceError(
                error=ErrorCode.INCORRECT_USERNAME_PASSWORD,
                debug_id=f"{DebugError.PASSWORD_VERIFY_FAILED}:{linenos}",
            )

        try:
            return AuthResponse.validate(account), None
        except Exception:
            linenos = trace_debugs(*sys.exc_info())
            return None, ServiceError(
                error=ErrorCode.TECHNICAL_ERROR,
                debug_id=f"{DebugError.PYDANTIC_VALIDATE_FAILED}:{linenos}",
            )
