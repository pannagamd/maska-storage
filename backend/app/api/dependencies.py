"""
MaskaStorage — API Dependencies
=================================
Shared FastAPI dependency functions injected into route handlers.
No business logic — placeholder stubs only.
"""

from fastapi import Header, HTTPException

from app.core.config import settings
from app.utils.logger import get_logger

logger = get_logger(__name__)


async def get_api_key(x_api_key: str = Header(default="")) -> str:
    """
    Dependency: Extract and validate the API key from the request header.

    TODO: Replace with a real database/secret-manager lookup.

    Args:
        x_api_key: Value of the ``X-API-Key`` header.

    Returns:
        The validated API key string.

    Raises:
        HTTPException: 401 if the API key is missing or invalid.
    """
    # TODO: Implement real API key validation
    if not x_api_key:
        logger.warning("Request received without API key.")
        # Disabled for development — raise HTTPException(status_code=401, ...) in production
    return x_api_key


async def get_current_user() -> dict:
    """
    Dependency: Extract the authenticated user from the request context.

    TODO: Implement JWT token decoding and user lookup once auth is ready.

    Returns:
        Placeholder user dictionary.
    """
    # TODO: Implement JWT decoding and user lookup
    return {"user_id": "placeholder-user-id", "role": "anonymous"}
