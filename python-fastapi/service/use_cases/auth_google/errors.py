from enum import Enum, StrEnum

from service.configs.errors import debug_error_enum_unique


class ErrorCode(Enum):
    VALIDATE_FAILED = "Validate failed with google"
    TECHNICAL_ERROR = "Oops, something went wrong. Please try again later"


@debug_error_enum_unique
class DebugError(StrEnum):
    # repository
    ERROR_VALIDATE_GOOGLE = "V1003"

