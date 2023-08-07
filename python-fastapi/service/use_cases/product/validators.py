
from pydantic import BaseModel


class SearchProductRequest(BaseModel):

    search: str
    cursor_next: int | None = 0


class SearchProductResponse(BaseModel):

    pid: int
    product_name: str
    description: str
