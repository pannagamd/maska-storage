"""
MaskaStorage — Document ORM Model
=====================================
Represents a document stored in the system.
No CRUD or business logic here — schema definition only.
"""

import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Document(Base):
    """
    ORM model for the ``document`` table.

    Stores metadata about every uploaded document.
    The actual file bytes are stored on disk / object storage,
    not in the database.
    """

    # ── Primary Key ────────────────────────────────────────────
    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        comment="UUID v4 document identifier.",
    )

    # ── File Metadata ──────────────────────────────────────────
    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="Original filename as provided by the uploader.",
    )
    file_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        comment="File extension / MIME type (e.g. 'pdf', 'docx').",
    )
    size_bytes: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
        comment="Size of the original file in bytes.",
    )
    storage_path: Mapped[str] = mapped_column(
        String(512),
        nullable=False,
        comment="Relative path to the stored file on disk or S3 key.",
    )

    # ── Processing State ───────────────────────────────────────
    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="pending",
        comment="Processing status: pending | processing | ready | failed.",
    )

    # ── Optional Metadata ──────────────────────────────────────
    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
        comment="Optional human-readable description.",
    )

    # ── Timestamps ─────────────────────────────────────────────
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        comment="UTC timestamp when the document was uploaded.",
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
        comment="UTC timestamp of the most recent update.",
    )

    def __repr__(self) -> str:  # pragma: no cover
        return f"<Document id={self.id!r} filename={self.filename!r} status={self.status!r}>"
