"""
MaskaStorage — Logging Utility
================================
Provides a reusable, structured logger for the entire backend application.
Uses Python's standard logging module with optional JSON formatting for
production environments.
"""

import logging
import sys
from typing import Optional

from app.core.config import settings


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Return a configured Logger instance.

    Args:
        name: Logger name, typically ``__name__`` of the calling module.
              If None, the root logger is returned.

    Returns:
        Configured :class:`logging.Logger` instance.

    Example::

        from app.utils.logger import get_logger

        logger = get_logger(__name__)
        logger.info("Application started")
    """
    logger = logging.getLogger(name or "maskaStorage")

    if not logger.handlers:
        _configure_logger(logger)

    return logger


def _configure_logger(logger: logging.Logger) -> None:
    """Attach handlers and set log level from application settings."""
    log_level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)
    logger.setLevel(log_level)

    # Console handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(log_level)

    if settings.APP_ENV == "production":
        # Use JSON formatter for structured logging in production
        formatter = _build_json_formatter()
    else:
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d — %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    # Prevent duplicate log records in child loggers
    logger.propagate = False


def _build_json_formatter() -> logging.Formatter:
    """Return a JSON-style log formatter for production use."""
    try:
        import json_log_formatter  # type: ignore[import]

        return json_log_formatter.JSONFormatter()
    except ImportError:
        # Fallback if json_log_formatter is not installed
        return logging.Formatter(
            fmt='{"time":"%(asctime)s","level":"%(levelname)s","module":"%(name)s","line":%(lineno)d,"message":"%(message)s"}',
            datefmt="%Y-%m-%dT%H:%M:%SZ",
        )
