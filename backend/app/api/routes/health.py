"""
MaskaStorage — Health Router
==============================
GET /api/v1/health

Returns a simple liveness check response.
No business logic — placeholder only.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.health import HealthResponse

router = APIRouter(prefix="/health", tags=["Health"])


@router.get(
    "",
    response_model=HealthResponse,
    summary="Health Check",
    description="Returns the current liveness status of the API server.",
)
async def health_check() -> JSONResponse:
    """
    Liveness check endpoint.

    Returns:
        JSON object with ``status: ok``.
    """
    return JSONResponse(content={"status": "ok"})
