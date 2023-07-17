from pydantic import BaseModel


class AuthRequest(BaseModel):

    """Login request from user."""

    username: str
    password: str


class AuthResponse(BaseModel):

    """Login response to user."""

    uid: int
    username: str
