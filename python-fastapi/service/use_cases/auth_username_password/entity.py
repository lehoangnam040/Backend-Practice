"""Account table to store user's account data."""
from pydantic import BaseModel


class Account(BaseModel):

    """Store user's account data."""

    uid: int
    username: str
    hashed_password: str
