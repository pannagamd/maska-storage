"""
MaskaStorage — Document Metadata Extractor Stub
=================================================
Responsible for extracting structured metadata from document content
(title, author, date, language, keywords, etc.).

TODO: Implement LLM-assisted and heuristic metadata extraction.
"""

from typing import Any

from app.utils.logger import get_logger

logger = get_logger(__name__)


class MetadataExtractor:
    """
    Extracts structured metadata from document text and file properties.

    TODO: Implement the following:
    - Heuristic extraction (regex for dates, emails, etc.)
    - LLM-assisted extraction for title, author, abstract
    - Language detection
    - Named entity recognition (NER) for organisations, people, places
    - Keyword extraction (TF-IDF, YAKE, KeyBERT)
    """

    async def extract(self, text: str, filename: str) -> dict[str, Any]:
        """
        Extract metadata from document text.

        TODO: Implement heuristic + LLM-based metadata extraction.

        Args:
            text: Cleaned document text.
            filename: Original filename (used as a fallback title source).

        Returns:
            Dictionary of extracted metadata fields.

        Raises:
            NotImplementedError: Until implementation is complete.
        """
        logger.debug("extract() called for filename=%s (stub — not implemented)", filename)
        raise NotImplementedError("MetadataExtractor.extract() is not yet implemented.")
