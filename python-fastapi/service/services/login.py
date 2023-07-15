import sys

from pydantic import BaseModel

from service.configs.errors import (
    DebugError,
    ServiceError,
    ServiceErrorCode,
    trace_debugs,
)
from service.configs.typing_compat import ResultWithErr
from service.repository import account_repository
from service.repository.interface.account import AccountRepository
from service.vendor.password import password_hasher
from service.vendor.password.interface import PasswordHasherInterface


class LoginV1RequestBody(BaseModel):

    """Login request from user."""

    username: str
    password: str


class LoginV1ResponseBody(BaseModel):

    """Login response to user."""

    uid: int
    username: str


class LoginService:
    def __init__(
        self: "LoginService",
        account_repository: AccountRepository,
        password_hasher: PasswordHasherInterface,
    ) -> None:
        self.account_repository = account_repository
        self.password_hasher = password_hasher

    async def login_by_username_password(
        self: "LoginService",
        request: LoginV1RequestBody,
    ) -> ResultWithErr[LoginV1ResponseBody]:
        try:
            account = await self.account_repository.get_an_account_by_username(
                request.username,
            )
        except Exception:
            linenos = trace_debugs(*sys.exc_info())
            return None, ServiceError(
                code=ServiceErrorCode.INCORRECT_USERNAME_PASSWORD,
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
                code=ServiceErrorCode.INCORRECT_USERNAME_PASSWORD,
                debug_id=f"{DebugError.PASSWORD_VERIFY_FAILED}:{linenos}",
            )

        try:
            return LoginV1ResponseBody.validate(account), None
        except Exception:
            linenos = trace_debugs(*sys.exc_info())
            return None, ServiceError(
                code=ServiceErrorCode.TECHNICAL_ERROR,
                debug_id=f"{DebugError.PYDANTIC_VALIDATE_FAILED}:{linenos}",
            )


login_v1_service = LoginService(account_repository, password_hasher)
