"""
MaskaStorage — Helper Utilities
=================================
General-purpose helper functions shared across the application.
No business logic — only pure utility functions.
"""

import hashlib
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def generate_uuid() -> str:
    """Generate a new random UUID v4 string."""
    return str(uuid.uuid4())


def utc_now() -> datetime:
    """Return the current UTC datetime (timezone-aware)."""
    return datetime.now(tz=timezone.utc)


def utc_timestamp() -> str:
    """Return the current UTC time as an ISO-8601 string."""
    return utc_now().isoformat()


def compute_file_hash(file_path: str | Path, algorithm: str = "sha256") -> str:
    """
    Compute the hash of a file on disk.

    Args:
        file_path: Absolute or relative path to the file.
        algorithm: Hashing algorithm (default: ``sha256``).

    Returns:
        Hex-digest string of the file hash.
    """
    h = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sanitize_filename(filename: str) -> str:
    """
    Remove unsafe characters from a filename, keeping only alphanumerics,
    dots, underscores, and hyphens.

    Args:
        filename: The original filename (e.g., from a file upload).

    Returns:
        A sanitised filename string.
    """
    import re

    # Keep the extension
    stem = Path(filename).stem
    suffix = Path(filename).suffix
    sanitized_stem = re.sub(r"[^\w\-]", "_", stem)
    return f"{sanitized_stem}{suffix}"


def flatten_dict(d: dict[str, Any], parent_key: str = "", sep: str = ".") -> dict[str, Any]:
    """
    Flatten a nested dictionary into a single-level dict using dot notation.

    Args:
        d: Dictionary to flatten.
        parent_key: Prefix for nested keys.
        sep: Key separator.

    Returns:
        Flat dictionary.
    """
    items: list[tuple[str, Any]] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def truncate_string(text: str, max_length: int = 200, suffix: str = "...") -> str:
    """
    Truncate a string to ``max_length`` characters, appending ``suffix``.

    Args:
        text: The input string.
        max_length: Maximum allowed length (including suffix).
        suffix: String to append when truncation occurs.

    Returns:
        Truncated (or original) string.
    """
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix
