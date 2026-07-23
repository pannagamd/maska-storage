from app.ai.url_scrapper.scraper import WebScraper
from app.ai.pdf_parser.parser import PDFParser
from app.ai.cleaner.cleaner import TextCleaner
from app.ai.chunker.chunker import TextChunker
from app.ai.embeddings.embeddings import EmbeddingGenerator
from app.ai.metadata.metadata import MetadataGenerator
from app.ai.summarizer.summarizer import DocumentSummarizer

class AIPipeline:
    """
    AIPipeline

    Responsible for:
    - Orchestrating the complete AI pipeline
    - Processing URLs
    - Processing PDFs
    - Returning structured AI results

    This module does NOT perform AI operations itself.
    It simply coordinates the individual AI modules.
    """

    def __init__(self):
        """
        Initializes every AI module once.

        Models such as the embedding model and Gemini client
        remain loaded and are reused for every request.
        """

        self.scraper = WebScraper()

        self.parser = PDFParser()

        self.cleaner = TextCleaner()

        self.chunker = TextChunker()

        self.embedder = EmbeddingGenerator()

        self.metadata = MetadataGenerator()

        self.summarizer = DocumentSummarizer()

    def process_url(self, url: str) -> dict:
        """
        Processes a webpage.

        Args:
            url (str): Webpage URL.

        Returns:
            dict: Complete AI pipeline output.
        """

        try:

            scraped = self.scraper.scrape(url)

            cleaned_text = self.cleaner.clean(
                scraped["text"]
            )

            chunks = self.chunker.chunk(
                cleaned_text
            )

            embedded_chunks = self.embedder.generate(
                chunks
            )

            metadata = self.metadata.generate(
                text=cleaned_text,
                title=scraped["title"],
                chunk_count=len(chunks)
            )

            summary = self.summarizer.summarize(
                cleaned_text
            )

            chunk_data = []

            embedding_data = []

            for item in embedded_chunks:

                chunk_data.append(
                    {
                        "chunk_id": item["chunk_id"],
                        "text": item["text"],
                        "length": item["length"]
                    }
                )

                embedding_data.append(
                    {
                        "chunk_id": item["chunk_id"],
                        "embedding": item["embedding"]
                    }
                )

            return {

                "source_type": "url",

                "document": {

                    "url": scraped["url"],

                    "title": scraped["title"],

                    "author": scraped["author"],

                    "date": scraped["date"],

                    "filename": None,

                    "page_count": None

                },

                "cleaned_text": cleaned_text,

                "chunks": chunk_data,

                "embeddings": embedding_data,

                "metadata": metadata,

                "summary": summary

            }

        except Exception as e:

            raise RuntimeError(
                f"URL Processing Error: {e}"
            )

    def process_pdf(self, pdf_path: str) -> dict:
        """
        Processes a PDF document.

        Args:
            pdf_path (str): PDF path.

        Returns:
            dict: Complete AI pipeline output.
        """

        try:

            parsed = self.parser.parse(
                pdf_path
            )

            cleaned_text = self.cleaner.clean(
                parsed["text"]
            )

            chunks = self.chunker.chunk(
                cleaned_text
            )

            embedded_chunks = self.embedder.generate(
                chunks
            )

            metadata = self.metadata.generate(
                text=cleaned_text,
                filename=parsed["filename"],
                chunk_count=len(chunks)
            )

            summary = self.summarizer.summarize(
                cleaned_text
            )

            chunk_data = []

            embedding_data = []

            for item in embedded_chunks:

                chunk_data.append(
                    {
                        "chunk_id": item["chunk_id"],
                        "text": item["text"],
                        "length": item["length"]
                    }
                )

                embedding_data.append(
                    {
                        "chunk_id": item["chunk_id"],
                        "embedding": item["embedding"]
                    }
                )

            return {

                "source_type": "pdf",

                "document": {

                    "url": None,

                    "title": None,

                    "author": None,

                    "date": None,

                    "filename": parsed["filename"],

                    "page_count": parsed["page_count"]

                },

                "cleaned_text": cleaned_text,

                "chunks": chunk_data,

                "embeddings": embedding_data,

                "metadata": metadata,

                "summary": summary

            }

        except Exception as e:

            raise RuntimeError(
                f"PDF Processing Error: {e}"
            )