"""Entrypoint of service."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def main() -> str:
    """Home page of service."""
    return "Service"


@router.get("/health")
async def health() -> dict:
    """Return health status of service."""
    return {"status": "OK"}
