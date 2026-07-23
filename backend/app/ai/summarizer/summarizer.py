import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


class DocumentSummarizer:
    """
    DocumentSummarizer

    Responsible for:
    - Loading the Gemini model
    - Generating document summaries
    - Returning the generated summary

    This module does NOT perform:
    - Chunking
    - Embedding generation
    - Metadata generation
    - Database storage
    """

    def __init__(
    self,
    model_name: str = "gemini-3.6-flash"
):
        """
        Initializes the Gemini client.

        Args:
            model_name (str): Gemini model name.
        """

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in environment variables."
            )

        self.client = genai.Client(api_key=api_key)

        self.model = model_name

    def summarize(self, text: str) -> dict:
        """
        Generates a concise summary.

        Args:
            text (str): Cleaned document text.

        Returns:
            dict: Generated summary.
        """

        try:

            if not isinstance(text, str):
                raise ValueError("Input must be a string.")

            if not text.strip():
                raise ValueError("Input text is empty.")

            prompt = f"""
You are an AI assistant for MaskaStorage.

Summarize the following document.

Requirements:
- Maximum 150 words
- Preserve all important ideas
- Do NOT invent information
- Use simple, professional language
- Return only the summary

Document:

{text}
"""

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            return {
                "summary": response.text.strip()
            }

        except Exception as e:
            raise RuntimeError(
                f"Summarization Error: {e}"
            )