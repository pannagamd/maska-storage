"""
MaskaStorage — Text Chunker Stub
===================================
Responsible for splitting cleaned text into overlapping chunks suitable
for embedding and vector storage.

TODO: Implement token-aware or sentence-aware chunking.
"""

from app.core.constants import DEFAULT_CHUNK_OVERLAP, DEFAULT_CHUNK_SIZE
from app.utils.logger import get_logger

logger = get_logger(__name__)


class TextChunker:
    """
    Splits cleaned document text into fixed-size, overlapping chunks.

    TODO: Implement the following strategies:
    - Fixed-size token chunking (default)
    - Sentence-boundary-aware chunking
    - Recursive character text splitter
    - Semantic chunking (embedding-similarity based)
    """

    def __init__(
        self,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
    ) -> None:
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk(self, text: str) -> list[str]:
        """
        Split ``text`` into a list of overlapping chunks.

        TODO: Implement token-aware splitting using tiktoken or similar.

        Args:
            text: Cleaned document text.

        Returns:
            Ordered list of text chunk strings.

        Raises:
            NotImplementedError: Until implementation is complete.
        """
        logger.debug(
            "chunk() called with chunk_size=%d overlap=%d (stub — not implemented)",
            self.chunk_size,
            self.chunk_overlap,
        )
        raise NotImplementedError("TextChunker.chunk() is not yet implemented.")
