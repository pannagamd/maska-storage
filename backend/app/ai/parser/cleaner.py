"""
MaskaStorage — Text Cleaner Stub
===================================
Responsible for normalising and cleaning raw extracted text before
chunking and embedding.

TODO: Implement whitespace normalisation, unicode normalisation,
      boilerplate removal, and language detection.
"""

from app.utils.logger import get_logger

logger = get_logger(__name__)


class TextCleaner:
    """
    Cleans and normalises raw extracted text.

    TODO: Implement the following:
    - Whitespace / newline normalisation
    - Unicode normalisation (NFC)
    - Remove headers, footers, page numbers
    - Remove excessive punctuation / special characters
    - Optional: language detection (langdetect / fasttext)
    """

    def clean(self, text: str) -> str:
        """
        Clean raw extracted text.

        TODO: Implement text normalisation pipeline.

        Args:
            text: Raw text extracted from a document.

        Returns:
            Cleaned, normalised text string.

        Raises:
            NotImplementedError: Until implementation is complete.
        """
        logger.debug("clean() called (stub — not implemented).")
        raise NotImplementedError("TextCleaner.clean() is not yet implemented.")
