"""
MaskaStorage — Exceptions Package
"""

from app.exceptions.exceptions import (
    AIServiceException,
    DatabaseException,
    FileTooLargeException,
    MaskaBaseException,
    NotFoundException,
    StorageException,
    UnsupportedFileTypeException,
    ValidationException,
)
from app.exceptions.handlers import register_exception_handlers

__all__ = [
    "MaskaBaseException",
    "NotFoundException",
    "ValidationException",
    "FileTooLargeException",
    "UnsupportedFileTypeException",
    "StorageException",
    "AIServiceException",
    "DatabaseException",
    "register_exception_handlers",
]
