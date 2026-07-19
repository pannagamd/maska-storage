"""
MaskaStorage — Chat Pydantic Schemas
"""

from pydantic import BaseModel, Field


class SourceDocument(BaseModel):
    """A source document chunk returned alongside a chat answer."""

    document_id: str = Field(..., description="ID of the source document.")
    filename: str = Field(..., description="Original filename of the source document.")
    excerpt: str = Field(..., description="Relevant text excerpt from the source document.")
    relevance_score: float = Field(
        ...,
        description="Relevance score of this chunk (0.0–1.0).",
        ge=0.0,
        le=1.0,
    )


class ChatRequest(BaseModel):
    """Request schema for POST /api/v1/chat."""

    query: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="The user's natural-language query.",
        examples=["What are the key findings in the Q4 report?"],
    )
    top_k: int = Field(
        default=5,
        ge=1,
        le=20,
        description="Maximum number of source documents to retrieve.",
    )
    include_sources: bool = Field(
        default=True,
        description="Whether to include source document excerpts in the response.",
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "query": "Summarise the key findings.",
                "top_k": 5,
                "include_sources": True,
            }
        }
    }


class ChatResponse(BaseModel):
    """Response schema for POST /api/v1/chat."""

    answer: str = Field(..., description="AI-generated answer to the user's query.")
    query: str = Field(..., description="The original user query echoed back.")
    sources: list[SourceDocument] = Field(
        default_factory=list,
        description="Source document chunks used to generate the answer.",
    )
    model: str = Field(..., description="Name of the LLM model used to generate the answer.")

    model_config = {
        "json_schema_extra": {
            "example": {
                "answer": "The key findings are...",
                "query": "Summarise the key findings.",
                "sources": [],
                "model": "gpt-4o",
            }
        }
    }
