"""Account table to store user's account data."""

from pydantic import BaseModel, TypeAdapter


class Product(BaseModel):
    """Store user's account data."""

    pid: int
    product_name: str
    description: str


ListProduct = TypeAdapter(list[Product])
