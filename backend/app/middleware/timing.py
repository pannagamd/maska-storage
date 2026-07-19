"""
MaskaStorage — Request Timing Middleware
=========================================
Measures and injects the processing time of each HTTP request into the
response as an ``X-Process-Time`` header (in milliseconds).
"""

import time

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.types import ASGIApp


class TimingMiddleware(BaseHTTPMiddleware):
    """Add ``X-Process-Time`` header (in ms) to every response."""

    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_time = time.perf_counter()
        response: Response = await call_next(request)
        elapsed_ms = (time.perf_counter() - start_time) * 1000
        response.headers["X-Process-Time"] = f"{elapsed_ms:.2f}ms"
        return response
