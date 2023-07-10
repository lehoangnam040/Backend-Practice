from pydantic import BaseModel


class ServiceError(BaseModel):

    code: str
    detail: str


NOT_FOUND_ACCOUNT_IN_DB = "NOT_FOUND_ACCOUNT_IN_DB"
PARSE_OBJECT_FAILED = "PARSE_OBJECT_FAILED"