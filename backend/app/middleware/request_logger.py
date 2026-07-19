"""
MaskaStorage — Request Logging Middleware
==========================================
Logs every incoming HTTP request and outgoing response (method, path,
status code, and duration).
"""

import time

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.types import ASGIApp

from app.utils.logger import get_logger

logger = get_logger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Log each request and its response status on completion."""

    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        logger.info(
            "→ %s %s  client=%s",
            request.method,
            request.url.path,
            request.client.host if request.client else "unknown",
        )

        response: Response = await call_next(request)

        logger.info(
            "← %s %s  status=%s",
            request.method,
            request.url.path,
            response.status_code,
        )
        return response
