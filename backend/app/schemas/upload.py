"""
MaskaStorage — Upload Pydantic Schemas
"""

from pydantic import BaseModel, Field


class UploadRequest(BaseModel):
    """
    Request metadata that accompanies a file upload.

    Note: The file itself is sent as a multipart form field, not JSON.
    This schema covers any additional JSON metadata in the request body.
    """

    tags: list[str] = Field(
        default_factory=list,
        description="Optional list of tags to associate with the document.",
        examples=[["research", "2024"]],
    )
    description: str | None = Field(
        default=None,
        max_length=500,
        description="Optional human-readable description of the document.",
    )


class UploadResponse(BaseModel):
    """Response schema for POST /api/v1/upload."""

    status: str = Field(
        ...,
        description="Upload acknowledgement status.",
        examples=["accepted"],
    )
    filename: str = Field(..., description="Original filename as provided by the client.")
    message: str = Field(..., description="Human-readable status message.")
    document_id: str = Field(
        ...,
        description="Unique identifier assigned to the uploaded document.",
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "status": "accepted",
                "filename": "report.pdf",
                "message": "File accepted for processing.",
                "document_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
            }
        }
    }
