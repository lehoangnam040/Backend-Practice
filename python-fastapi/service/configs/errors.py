from enum import Enum, StrEnum
from types import TracebackType

from pydantic import BaseModel


def trace_debugs(
    _: type[BaseException] | None,
    __: BaseException | None,
    tb: TracebackType | None,
) -> str:
    linenos = []
    print("===============================")
    while tb:
        print(tb.tb_frame.f_code.co_filename, tb.tb_frame.f_code.co_name, tb.tb_lineno)
        linenos.append(tb.tb_lineno)
        tb = tb.tb_next
    print("===============================")
    return ".".join(map(str, linenos))


class ServiceError(BaseModel):
    code: Enum
    debug_id: str


class ServiceErrorCode(Enum):
    INCORRECT_USERNAME_PASSWORD = "Incorrect username or password"
    TECHNICAL_ERROR = "Oops, something went wrong. Please try again later"


class DebugError(StrEnum):
    # repository
    NOT_FOUND_ON_DB = "R1001"

    # vendor
    PYDANTIC_VALIDATE_FAILED = "V1001"
    PASSWORD_VERIFY_FAILED = "V1002"
