"""
MaskaStorage — Chat Router
============================
POST /api/v1/chat

Accepts a user query and returns a placeholder RAG response.
No business logic — placeholder only.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post(
    "",
    response_model=ChatResponse,
    summary="Chat with Documents",
    description="Send a query and receive an AI-generated answer grounded in archived documents (placeholder).",
)
async def chat(request: ChatRequest) -> JSONResponse:
    """
    Handle a chat/query request.

    TODO: Implement RAG pipeline: retrieve → rerank → generate.

    Args:
        request: The chat request containing the user query.

    Returns:
        Placeholder chat response.
    """
    return JSONResponse(
        content={
            "answer": "This is a placeholder response. The RAG pipeline is not yet implemented.",
            "query": request.query,
            "sources": [],
            "model": "placeholder",
        }
    )
