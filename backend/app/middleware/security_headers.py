"""
MaskaStorage — Security Headers Middleware
===========================================
Injects common security-related HTTP response headers on every request
to mitigate common web vulnerabilities (XSS, clickjacking, sniffing, etc.).
"""

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.types import ASGIApp

_SECURITY_HEADERS: dict[str, str] = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "X-XSS-Protection": "1; mode=block",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Permissions-Policy": "geolocation=(), microphone=(), camera=()",
    "Strict-Transport-Security": "max-age=63072000; includeSubDomains; preload",
    "Content-Security-Policy": "default-src 'self'",
}


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Inject standard security headers into every HTTP response."""

    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        response: Response = await call_next(request)
        for header, value in _SECURITY_HEADERS.items():
            response.headers[header] = value
        return response
