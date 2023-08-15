from enum import Enum, StrEnum

from service.configs.errors import debug_error_enum_unique


class ErrorCode(Enum):
    TECHNICAL_ERROR = "Oops, something went wrong. Please try again later"


@debug_error_enum_unique
class DebugError(StrEnum):
    # vendor
    PYDANTIC_VALIDATE_FAILED = "V1003"
