"""
MaskaStorage — Archive Router
================================
GET  /api/v1/archive       → list all archived documents (placeholder)
GET  /api/v1/archive/{id}  → get a single document by ID (placeholder)
DELETE /api/v1/archive/{id} → delete a document by ID (placeholder)

No business logic — placeholder only.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.archive import ArchiveResponse

router = APIRouter(prefix="/archive", tags=["Archive"])


@router.get(
    "",
    response_model=ArchiveResponse,
    summary="List Archived Documents",
    description="Retrieve a paginated list of all archived documents (placeholder).",
)
async def list_archive() -> JSONResponse:
    """
    List all documents in the archive.

    TODO: Implement database query with pagination and filtering.

    Returns:
        Placeholder list response.
    """
    return JSONResponse(
        content={
            "items": [],
            "total": 0,
            "page": 1,
            "page_size": 20,
            "message": "Archive listing — not yet implemented.",
        }
    )


@router.get(
    "/{document_id}",
    summary="Get Archived Document",
    description="Retrieve a single archived document by its ID (placeholder).",
)
async def get_archive_item(document_id: str) -> JSONResponse:
    """
    Retrieve a specific archived document.

    TODO: Implement database lookup by ID.

    Args:
        document_id: Unique identifier of the document.

    Returns:
        Placeholder item response.
    """
    return JSONResponse(
        content={
            "document_id": document_id,
            "message": "Single document retrieval — not yet implemented.",
        }
    )


@router.delete(
    "/{document_id}",
    summary="Delete Archived Document",
    description="Delete an archived document by its ID (placeholder).",
    status_code=202,
)
async def delete_archive_item(document_id: str) -> JSONResponse:
    """
    Delete a specific archived document.

    TODO: Implement cascade delete (DB record + vector store + files).

    Args:
        document_id: Unique identifier of the document.

    Returns:
        Placeholder deletion response.
    """
    return JSONResponse(
        status_code=202,
        content={
            "document_id": document_id,
            "message": "Document deletion — not yet implemented.",
        },
    )
