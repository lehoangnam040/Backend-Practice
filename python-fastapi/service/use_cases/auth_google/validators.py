from pydantic import BaseModel


class AuthResponse(BaseModel):

    """Login response to user."""

    uid: int
    username: str
