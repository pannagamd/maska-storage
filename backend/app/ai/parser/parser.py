"""
MaskaStorage — Document Parser Stub
======================================
Responsible for extracting plain text from raw document bytes.

TODO: Implement parsers for PDF (pdfplumber/pypdf), DOCX (python-docx),
      Markdown, HTML (BeautifulSoup), and plain text.
"""

from app.utils.logger import get_logger

logger = get_logger(__name__)


class DocumentParser:
    """
    Extracts structured text content from raw document bytes.

    TODO: Implement the following per file type:
    - PDF: page-by-page text extraction
    - DOCX: paragraph and table extraction
    - HTML: tag stripping, main content isolation
    - Markdown: frontmatter stripping
    - TXT: direct read with encoding detection
    """

    async def parse(self, content: bytes, file_type: str) -> str:
        """
        Parse raw document bytes into plain text.

        TODO: Route to the correct parser based on ``file_type``.

        Args:
            content: Raw bytes of the document file.
            file_type: File extension (e.g., ``pdf``, ``docx``, ``txt``).

        Returns:
            Extracted plain text content.

        Raises:
            NotImplementedError: Until implementation is complete.
        """
        logger.debug(
            "parse() called for file_type=%s, content_size=%d bytes (stub — not implemented)",
            file_type,
            len(content),
        )
        raise NotImplementedError("DocumentParser.parse() is not yet implemented.")
