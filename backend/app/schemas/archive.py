"""
MaskaStorage — Archive Pydantic Schemas
"""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class ArchiveItem(BaseModel):
    """Represents a single archived document in the system."""

    document_id: str = Field(..., description="Unique identifier of the document.")
    filename: str = Field(..., description="Original filename of the document.")
    file_type: str = Field(..., description="MIME type or extension of the document.")
    size_bytes: int = Field(..., description="Size of the document in bytes.", ge=0)
    status: str = Field(
        ...,
        description="Processing status of the document.",
        examples=["pending", "processing", "ready", "failed"],
    )
    tags: list[str] = Field(default_factory=list, description="Tags associated with the document.")
    description: str | None = Field(default=None, description="Optional document description.")
    created_at: datetime = Field(..., description="UTC timestamp when the document was uploaded.")
    updated_at: datetime = Field(..., description="UTC timestamp of the last status update.")
    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Arbitrary metadata extracted from the document.",
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "document_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
                "filename": "report.pdf",
                "file_type": "pdf",
                "size_bytes": 204800,
                "status": "ready",
                "tags": ["research"],
                "description": "Q4 Financial Report",
                "created_at": "2024-01-15T10:30:00Z",
                "updated_at": "2024-01-15T10:31:00Z",
                "metadata": {"pages": 12, "author": "Alice"},
            }
        }
    }


class ArchiveResponse(BaseModel):
    """Paginated list response for GET /api/v1/archive."""

    items: list[ArchiveItem] = Field(default_factory=list, description="List of archived documents.")
    total: int = Field(..., description="Total number of documents matching the query.", ge=0)
    page: int = Field(..., description="Current page number (1-indexed).", ge=1)
    page_size: int = Field(..., description="Number of items per page.", ge=1)
    message: str | None = Field(default=None, description="Optional status message.")
