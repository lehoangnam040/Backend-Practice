from .interface import PasswordHasherInterface


def _factory(using: str) -> PasswordHasherInterface:
    if using == "bcrypt":
        from .bcrypt import BcryptPasslibPasswordHasher

        return BcryptPasslibPasswordHasher()
    raise NotImplementedError


password_hasher = _factory("bcrypt")
