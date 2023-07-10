from passlib.context import CryptContext


class BcryptPasslibPasswordHasher:
    def __init__(self: "BcryptPasslibPasswordHasher") -> None:
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(
        self: "BcryptPasslibPasswordHasher",
        password: str,
    ) -> tuple[Exception | None, str | None]:
        try:
            return None, self.pwd_context.hash(password)
        except (TypeError, ValueError) as err:
            return err, None

    def verify_hashed_password(
        self: "BcryptPasslibPasswordHasher",
        password: str,
        hashed_password: str,
    ) -> tuple[Exception | None, bool | None]:
        try:
            return None, self.pwd_context.verify(password, hashed_password)
        except (TypeError, ValueError) as err:
            return err, None
