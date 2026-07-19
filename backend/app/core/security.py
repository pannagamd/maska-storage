"""
MaskaStorage — Security Utilities
===================================
Placeholder security helpers for API key verification, secret-key
operations, and future authentication flows.

All actual secrets must be supplied via environment variables — never
hard-coded here.
"""

from app.core.config import settings
from app.utils.logger import get_logger

logger = get_logger(__name__)


def verify_api_key(api_key: str) -> bool:
    """
    Verify that the provided API key is valid.

    TODO: Replace this placeholder check with a database lookup or
          secret manager integration once authentication is implemented.

    Args:
        api_key: The raw API key from the request header.

    Returns:
        ``True`` if the key is valid, ``False`` otherwise.
    """
    # TODO: Implement real API key verification
    logger.debug("API key verification requested (stub — always returns False for safety).")
    return False


def hash_secret(value: str) -> str:
    """
    Hash a secret value (e.g., API key) using SHA-256 + a salt derived
    from ``SECRET_KEY`` before storing it in the database.

    TODO: Use bcrypt or argon2 for passwords.

    Args:
        value: The raw secret to hash.

    Returns:
        Hex-digest string of the hashed value.
    """
    import hashlib

    # TODO: Replace with a proper KDF (e.g., argon2, bcrypt)
    salt = settings.SECRET_KEY.encode()
    return hashlib.sha256(salt + value.encode()).hexdigest()
