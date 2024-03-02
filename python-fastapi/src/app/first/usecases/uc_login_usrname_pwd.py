import sys
from typing import Protocol, runtime_checkable

from pydantic import BaseModel

from src.app.first.entity.account import Account
from src.error import ServiceError, trace_debugs
from src.types import ResultWithErr

from .errors import DebugError, ErrorCode


class Request(BaseModel):
    """Login request from user."""

    username: str
    password: str


class Response(BaseModel):
    """Login response to user."""

    uid: int
    username: str


@runtime_checkable
class _PasswordHasher(Protocol):
    def hash_password(
        self: "_PasswordHasher",
        password: str,
    ) -> str: ...

    def verify_hashed_password(
        self: "_PasswordHasher",
        password: str,
        hashed_password: str,
    ) -> bool: ...


@runtime_checkable
class _Repository(Protocol):
    async def get_an_account_by_username(
        self: "_Repository",
        username: str,
    ) -> Account:
        """Get account from database by unique username.

        If any reason causes multiple username, return first result.
        """
        ...


class Usecase:
    def __init__(
        self: "Usecase",
        account_repository: _Repository,
        password_hasher: _PasswordHasher,
    ) -> None:
        self.account_repository = account_repository
        self.password_hasher = password_hasher

    async def logic(
        self: "Usecase",
        request: Request,
    ) -> ResultWithErr[Response]:
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
            if not success:
                msg = "not success when verify"
                raise Exception(msg)
        except Exception:
            linenos = trace_debugs(*sys.exc_info())
            return None, ServiceError(
                error=ErrorCode.INCORRECT_USERNAME_PASSWORD,
                debug_id=f"{DebugError.PASSWORD_VERIFY_FAILED}:{linenos}",
            )

        try:
            return Response.model_validate(account, from_attributes=True), None
        except Exception:
            linenos = trace_debugs(*sys.exc_info())
            return None, ServiceError(
                error=ErrorCode.TECHNICAL_ERROR,
                debug_id=f"{DebugError.PYDANTIC_VALIDATE_FAILED}:{linenos}",
            )
