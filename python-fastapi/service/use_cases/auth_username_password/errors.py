from enum import Enum, StrEnum

from service.configs.errors import debug_error_enum_unique, service_error_enum_unique


@service_error_enum_unique
class ErrorCode(Enum):
    INCORRECT_USERNAME_PASSWORD = "Incorrect username or password"
    TECHNICAL_ERROR = "Oops, something went wrong. Please try again later"


@debug_error_enum_unique
class DebugError(StrEnum):
    # repository
    NOT_FOUND_ON_DB = "R1001"

    # vendor
    PYDANTIC_VALIDATE_FAILED = "V1001"
    PASSWORD_VERIFY_FAILED = "V1002"
