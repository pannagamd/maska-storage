"""
MaskaStorage — Validator Utilities
=====================================
Input validation helpers used by API endpoints and service layers.
No business logic — only data validation functions.
"""

import re
from pathlib import Path
from typing import Any

from app.core.constants import ALLOWED_FILE_EXTENSIONS, MAX_UPLOAD_SIZE_BYTES


def is_valid_email(email: str) -> bool:
    """
    Check whether ``email`` is a syntactically valid email address.

    Args:
        email: Email string to validate.

    Returns:
        ``True`` if valid, ``False`` otherwise.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))


def is_valid_uuid(value: str) -> bool:
    """
    Check whether ``value`` is a valid UUID v4 string.

    Args:
        value: String to check.

    Returns:
        ``True`` if valid UUID, ``False`` otherwise.
    """
    import uuid

    try:
        uuid.UUID(str(value), version=4)
        return True
    except ValueError:
        return False


def is_allowed_file_type(filename: str) -> bool:
    """
    Validate that the file extension is in the allow-list.

    Args:
        filename: Original filename including extension.

    Returns:
        ``True`` if the extension is permitted, ``False`` otherwise.
    """
    ext = Path(filename).suffix.lstrip(".").lower()
    return ext in ALLOWED_FILE_EXTENSIONS


def is_within_size_limit(size_bytes: int) -> bool:
    """
    Check that a file size does not exceed the configured maximum.

    Args:
        size_bytes: File size in bytes.

    Returns:
        ``True`` if within limit, ``False`` otherwise.
    """
    return 0 < size_bytes <= MAX_UPLOAD_SIZE_BYTES


def is_non_empty_string(value: Any) -> bool:
    """Return ``True`` if ``value`` is a non-empty, non-whitespace string."""
    return isinstance(value, str) and bool(value.strip())


def is_positive_integer(value: Any) -> bool:
    """Return ``True`` if ``value`` is an integer greater than zero."""
    return isinstance(value, int) and value > 0


def validate_pagination(page: int, page_size: int) -> tuple[bool, str]:
    """
    Validate pagination parameters.

    Args:
        page: Current page number (1-indexed).
        page_size: Number of items per page.

    Returns:
        Tuple of (is_valid, error_message). ``error_message`` is empty string
        when ``is_valid`` is ``True``.
    """
    if page < 1:
        return False, "page must be >= 1"
    if not (1 <= page_size <= 100):
        return False, "page_size must be between 1 and 100"
    return True, ""
