"""Account table to store user's account data."""
from pydantic import BaseModel


class Product(BaseModel):

    """Store user's account data."""

    pid: int
    product_name: str
    description: str
