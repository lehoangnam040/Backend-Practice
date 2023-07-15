from passlib.context import CryptContext


class BcryptPasslibPasswordHasher:
    def __init__(self: "BcryptPasslibPasswordHasher") -> None:
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(
        self: "BcryptPasslibPasswordHasher",
        password: str,
    ) -> str:
        return self.pwd_context.hash(password)

    def verify_hashed_password(
        self: "BcryptPasslibPasswordHasher",
        password: str,
        hashed_password: str,
    ) -> bool:
        return self.pwd_context.verify(password, hashed_password)
