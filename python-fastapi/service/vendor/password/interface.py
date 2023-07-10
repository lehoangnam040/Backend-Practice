from typing import Protocol, runtime_checkable


@runtime_checkable
class PasswordHasherInterface(Protocol):
    def hash_password(
        self: "PasswordHasherInterface",
        password: str,
    ) -> tuple[Exception | None, str | None]:
        ...

    def verify_hashed_password(
        self: "PasswordHasherInterface",
        password: str,
        hashed_password: str,
    ) -> tuple[Exception | None, bool | None]:
        ...
