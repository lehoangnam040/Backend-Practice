from pydantic import BaseModel
from pydantic.errors import DictError

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
    ) -> tuple[Exception | None, LoginV1ResponseBody | None]:
        account, err = await self.account_repository.get_an_account_by_username(
            request.username,
        )
        if err is not None:
            return Exception("not found"), None
        if account is None:
            return Exception("not found"), None
        err, success = self.password_hasher.verify_hashed_password(
            request.password,
            account.hashed_password,
        )
        if err is not None:
            return Exception("password not same"), None
        if not success:
            return Exception("verify password failed"), None

        try:
            return None, LoginV1ResponseBody.validate(account)
        except (DictError, Exception) as err:
            return err, None


login_v1_service = LoginService(account_repository, password_hasher)
