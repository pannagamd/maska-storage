"""
MaskaStorage — FastAPI Application Entry Point
================================================
Creates the FastAPI app, registers all middleware, exception handlers,
and API routers.

Run locally with::

    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
"""

from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.routes import archive, chat, health, upload
from app.core.config import settings
from app.core.constants import API_V1_PREFIX, APP_DESCRIPTION, APP_TITLE
from app.exceptions.handlers import register_exception_handlers
from app.middleware.cors import add_cors_middleware
from app.middleware.request_logger import RequestLoggingMiddleware
from app.middleware.security_headers import SecurityHeadersMiddleware
from app.middleware.timing import TimingMiddleware
from app.utils.logger import get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """
    Application lifespan handler.

    - **Startup**: initialise database connections, vector store, etc.
    - **Shutdown**: cleanly close all connections.

    TODO: Add real initialisation logic when components are implemented.
    """
    logger.info("Starting up %s v%s (%s)", settings.APP_NAME, settings.APP_VERSION, settings.APP_ENV)
    # TODO: initialise DB, vector store, caches, etc.
    yield
    logger.info("Shutting down %s.", settings.APP_NAME)
    # TODO: close DB connections, flush caches, etc.


def create_app() -> FastAPI:
    """
    Application factory — create and configure the FastAPI instance.

    Returns:
        Fully configured :class:`FastAPI` application.
    """
    app = FastAPI(
        title=APP_TITLE,
        description=APP_DESCRIPTION,
        version=settings.APP_VERSION,
        docs_url="/docs" if settings.DEBUG else None,
        redoc_url="/redoc" if settings.DEBUG else None,
        lifespan=lifespan,
    )

    # ── Middleware (applied in reverse registration order) ───────────────────
    add_cors_middleware(app)
    app.add_middleware(SecurityHeadersMiddleware)
    app.add_middleware(TimingMiddleware)
    app.add_middleware(RequestLoggingMiddleware)

    # ── Exception Handlers ───────────────────────────────────────────────────
    register_exception_handlers(app)

    # ── API Routers ──────────────────────────────────────────────────────────
    app.include_router(health.router, prefix=API_V1_PREFIX)
    app.include_router(upload.router, prefix=API_V1_PREFIX)
    app.include_router(archive.router, prefix=API_V1_PREFIX)
    app.include_router(chat.router, prefix=API_V1_PREFIX)

    # ── Root redirect ────────────────────────────────────────────────────────
    @app.get("/", include_in_schema=False)
    async def root() -> JSONResponse:
        return JSONResponse(
            content={
                "name": APP_TITLE,
                "version": settings.APP_VERSION,
                "docs": "/docs",
                "health": f"{API_V1_PREFIX}/health",
            }
        )

    return app


app: FastAPI = create_app()
