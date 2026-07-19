"""
MaskaStorage — Health Pydantic Schemas
"""

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Response schema for GET /api/v1/health."""

    status: str = Field(
        ...,
        description="Liveness status of the API server.",
        examples=["ok"],
    )

    model_config = {"json_schema_extra": {"example": {"status": "ok"}}}
