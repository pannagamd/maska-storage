"""
MaskaStorage — CORS Middleware Configuration
=============================================
Configures Cross-Origin Resource Sharing using FastAPI's built-in
CORSMiddleware.  Allowed origins are read from application settings.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings


def add_cors_middleware(app: FastAPI) -> None:
    """
    Attach CORS middleware to the FastAPI application.

    Args:
        app: The FastAPI application instance.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )
