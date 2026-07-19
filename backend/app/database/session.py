"""
MaskaStorage — Database Session Management
============================================
Configures the async SQLAlchemy engine and session factory.
Provides a ``get_db`` dependency for use in FastAPI route handlers.

No CRUD or business logic here.
"""

from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import settings
from app.utils.logger import get_logger

logger = get_logger(__name__)

# ─── Engine ──────────────────────────────────────────────────────────────────
engine: AsyncEngine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,  # Log SQL statements in debug mode
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    pool_pre_ping=True,   # Recycle stale connections
)

# ─── Session Factory ─────────────────────────────────────────────────────────
AsyncSessionLocal: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)


async def get_db() -> AsyncIterator[AsyncSession]:
    """
    FastAPI dependency that yields an :class:`AsyncSession`.

    Usage in a route::

        @router.get("/example")
        async def example(db: AsyncSession = Depends(get_db)):
            ...

    Yields:
        An active :class:`AsyncSession` that is automatically closed after
        the request completes.  Rolls back on unhandled exceptions.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
