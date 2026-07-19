"""
MaskaStorage — Vector Store Stub
====================================
Provides an abstract interface and stub implementation for vector storage
and similarity search operations.

TODO: Implement adapters for ChromaDB, Pinecone, Weaviate, or pgvector.
"""

from abc import ABC, abstractmethod
from typing import Any

from app.utils.logger import get_logger

logger = get_logger(__name__)


class VectorStore(ABC):
    """
    Abstract base class for all vector store backends.

    TODO: Implement concrete subclasses for:
    - ChromaDB (local development)
    - Pinecone (cloud production)
    - pgvector (PostgreSQL extension)
    - FAISS (in-memory / file-based)
    """

    @abstractmethod
    async def upsert(
        self,
        ids: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict[str, Any]],
        texts: list[str],
    ) -> None:
        """
        Insert or update vectors with associated metadata.

        TODO: Implement backend-specific upsert logic.

        Args:
            ids: Unique identifiers for each vector.
            embeddings: Dense vector embeddings.
            metadatas: Metadata dictionaries for each vector.
            texts: Original text chunks corresponding to each embedding.
        """

    @abstractmethod
    async def query(
        self,
        query_embedding: list[float],
        top_k: int = 5,
        filters: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        """
        Find the top-k most similar vectors to the query embedding.

        TODO: Implement similarity search with optional metadata filtering.

        Args:
            query_embedding: The query vector.
            top_k: Number of results to return.
            filters: Optional metadata filters.

        Returns:
            List of result dicts with ``id``, ``score``, ``text``, ``metadata``.
        """

    @abstractmethod
    async def delete(self, ids: list[str]) -> None:
        """
        Delete vectors by their IDs.

        TODO: Implement backend-specific deletion.

        Args:
            ids: List of vector IDs to delete.
        """


class StubVectorStore(VectorStore):
    """
    Stub implementation of :class:`VectorStore`.
    Raises :exc:`NotImplementedError` on every method call.
    Replace with a real backend implementation.
    """

    async def upsert(
        self,
        ids: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict[str, Any]],
        texts: list[str],
    ) -> None:
        logger.debug("StubVectorStore.upsert() called — not implemented.")
        raise NotImplementedError("VectorStore.upsert() is not yet implemented.")

    async def query(
        self,
        query_embedding: list[float],
        top_k: int = 5,
        filters: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        logger.debug("StubVectorStore.query() called — not implemented.")
        raise NotImplementedError("VectorStore.query() is not yet implemented.")

    async def delete(self, ids: list[str]) -> None:
        logger.debug("StubVectorStore.delete() called — not implemented.")
        raise NotImplementedError("VectorStore.delete() is not yet implemented.")
