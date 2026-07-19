"""
MaskaStorage — Application Configuration
==========================================
Uses pydantic-settings to load and validate all environment variables.
Values are read from the ``.env`` file in the backend directory.
"""

from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application-wide settings loaded from environment variables / .env file.

    All fields have sensible defaults for local development.
    Override via environment variables or a ``.env`` file in ``backend/``.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ── Application ─────────────────────────────────────
    APP_NAME: str = "MaskaStorage"
    APP_VERSION: str = "0.1.0"
    APP_ENV: str = "development"
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"

    # ── API Server ───────────────────────────────────────
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    API_PREFIX: str = "/api/v1"

    # ── CORS ─────────────────────────────────────────────
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]

    # ── Database ─────────────────────────────────────────
    DATABASE_URL: str = "sqlite+aiosqlite:///./maskadb.sqlite"
    DATABASE_POOL_SIZE: int = 5
    DATABASE_MAX_OVERFLOW: int = 10

    # ── OpenAI / LLM ─────────────────────────────────────
    OPENAI_API_KEY: str = "sk-placeholder"
    OPENAI_MODEL: str = "gpt-4o"
    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-small"
    OPENAI_MAX_TOKENS: int = 2048
    OPENAI_TEMPERATURE: float = 0.7

    # ── Vector Store ─────────────────────────────────────
    VECTOR_STORE_TYPE: str = "chromadb"
    CHROMADB_HOST: str = "localhost"
    CHROMADB_PORT: int = 8001
    PINECONE_API_KEY: str = "placeholder"
    PINECONE_INDEX_NAME: str = "maska-index"

    # ── Storage ──────────────────────────────────────────
    UPLOAD_DIR: str = "app/data/uploads"
    PROCESSED_DIR: str = "app/data/processed"
    CACHE_DIR: str = "app/data/cache"
    MAX_UPLOAD_SIZE_MB: int = 50
    ALLOWED_FILE_TYPES: str = "pdf,docx,txt,md,html"

    # ── Security ─────────────────────────────────────────
    SECRET_KEY: str = "changeme-super-secret-key"
    API_KEY_HEADER: str = "X-API-Key"
    RATE_LIMIT_PER_MINUTE: int = 60

    # ── AWS (optional) ───────────────────────────────────
    AWS_ACCESS_KEY_ID: str = "placeholder"
    AWS_SECRET_ACCESS_KEY: str = "placeholder"
    AWS_REGION: str = "us-east-1"
    S3_BUCKET_NAME: str = "maska-storage-bucket"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """
    Return a cached :class:`Settings` instance.

    Use this function instead of constructing ``Settings()`` directly so
    that environment variables are only read once per process.
    """
    return Settings()


# Module-level singleton — imported directly by the rest of the app
settings: Settings = get_settings()
