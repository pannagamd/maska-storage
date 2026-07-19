"""
MaskaStorage — Upload Router
==============================
POST /api/v1/upload

Accepts a file and returns a placeholder acknowledgement.
No business logic — placeholder only.
"""

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

from app.schemas.upload import UploadResponse

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post(
    "",
    response_model=UploadResponse,
    summary="Upload Document",
    description="Upload a document for storage, parsing, and embedding (placeholder).",
    status_code=202,
)
async def upload_document(file: UploadFile = File(...)) -> JSONResponse:
    """
    Accept a file upload.

    TODO: Implement file validation, storage, parsing pipeline.

    Args:
        file: The uploaded file from the multipart form.

    Returns:
        Placeholder 202 Accepted response.
    """
    return JSONResponse(
        status_code=202,
        content={
            "status": "accepted",
            "filename": file.filename,
            "message": "File accepted for processing.",
            "document_id": "placeholder-document-id",
        },
    )
