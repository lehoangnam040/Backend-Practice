from __future__ import annotations

from enum import Enum, StrEnum


class ErrorCode(Enum):
    VALIDATE_FAILED = "Validate failed with google"
    INCORRECT_USERNAME_PASSWORD = "Incorrect username or password"
    TECHNICAL_ERROR = "Oops, something went wrong. Please try again later"


class DebugError(StrEnum):
    # repository
    NOT_FOUND_ON_DB = "R1001"

    # vendor
    PYDANTIC_VALIDATE_FAILED = "V1001"
    PASSWORD_VERIFY_FAILED = "V1002"
    ERROR_VALIDATE_GOOGLE = "V1003"
