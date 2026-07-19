"""
MaskaStorage — Core Package
"""

from app.core.config import settings
from app.core.constants import (
    API_V1_PREFIX,
    APP_DESCRIPTION,
    APP_TITLE,
    MAX_UPLOAD_SIZE_BYTES,
)

__all__ = [
    "settings",
    "APP_TITLE",
    "APP_DESCRIPTION",
    "API_V1_PREFIX",
    "MAX_UPLOAD_SIZE_BYTES",
]
