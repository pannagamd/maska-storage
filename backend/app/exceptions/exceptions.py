"""
MaskaStorage — Custom Exceptions
==================================
Defines application-specific exceptions that map to HTTP error responses.
"""


class MaskaBaseException(Exception):
    """Base exception for all MaskaStorage application errors."""

    status_code: int = 500
    detail: str = "An unexpected error occurred."

    def __init__(self, detail: str | None = None) -> None:
        self.detail = detail or self.__class__.detail
        super().__init__(self.detail)


class NotFoundException(MaskaBaseException):
    """Raised when a requested resource cannot be found (HTTP 404)."""

    status_code = 404
    detail = "The requested resource was not found."


class ValidationException(MaskaBaseException):
    """Raised when request data fails validation (HTTP 422)."""

    status_code = 422
    detail = "Request validation failed."


class FileTooLargeException(MaskaBaseException):
    """Raised when an uploaded file exceeds the size limit (HTTP 413)."""

    status_code = 413
    detail = "The uploaded file exceeds the maximum allowed size."


class UnsupportedFileTypeException(MaskaBaseException):
    """Raised when an uploaded file has a disallowed extension (HTTP 415)."""

    status_code = 415
    detail = "The file type is not supported."


class StorageException(MaskaBaseException):
    """Raised when a file storage operation fails (HTTP 500)."""

    status_code = 500
    detail = "A storage error occurred."


class AIServiceException(MaskaBaseException):
    """Raised when an AI/LLM service call fails (HTTP 503)."""

    status_code = 503
    detail = "The AI service is temporarily unavailable."


class DatabaseException(MaskaBaseException):
    """Raised when a database operation fails (HTTP 500)."""

    status_code = 500
    detail = "A database error occurred."
