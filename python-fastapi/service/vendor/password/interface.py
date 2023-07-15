from typing import Protocol, runtime_checkable


@runtime_checkable
class PasswordHasherInterface(Protocol):
    def hash_password(
        self: "PasswordHasherInterface",
        password: str,
    ) -> str:
        ...

    def verify_hashed_password(
        self: "PasswordHasherInterface",
        password: str,
        hashed_password: str,
    ) -> bool:
        ...
