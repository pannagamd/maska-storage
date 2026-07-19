"""
MaskaStorage — Global Exception Handlers
==========================================
Registers FastAPI exception handlers that convert application exceptions
and unexpected errors into consistent JSON error responses.
"""

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.exceptions.exceptions import MaskaBaseException
from app.utils.logger import get_logger

logger = get_logger(__name__)


def _error_response(status_code: int, detail: str, request: Request) -> JSONResponse:
    """Build a standardised JSON error response."""
    return JSONResponse(
        status_code=status_code,
        content={
            "error": True,
            "status_code": status_code,
            "detail": detail,
            "path": str(request.url.path),
        },
    )


async def maska_exception_handler(request: Request, exc: MaskaBaseException) -> JSONResponse:
    """Handle all custom MaskaStorage application exceptions."""
    logger.warning(
        "Application exception: %s — %s [%s %s]",
        type(exc).__name__,
        exc.detail,
        request.method,
        request.url.path,
    )
    return _error_response(exc.status_code, exc.detail, request)


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    """Handle Pydantic/FastAPI request validation errors."""
    errors = exc.errors()
    detail = "; ".join(
        f"{'.'.join(str(loc) for loc in e['loc'])}: {e['msg']}" for e in errors
    )
    logger.warning("Validation error on %s %s: %s", request.method, request.url.path, detail)
    return _error_response(422, detail, request)


async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Catch-all handler for any unexpected errors."""
    logger.exception(
        "Unhandled exception on %s %s: %s", request.method, request.url.path, exc
    )
    return _error_response(500, "An unexpected internal error occurred.", request)


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register all global exception handlers on the FastAPI application.

    Call this during application startup in ``main.py``.
    """
    app.add_exception_handler(MaskaBaseException, maska_exception_handler)  # type: ignore[arg-type]
    app.add_exception_handler(RequestValidationError, validation_exception_handler)  # type: ignore[arg-type]
    app.add_exception_handler(Exception, unhandled_exception_handler)
