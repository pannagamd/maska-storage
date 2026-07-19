"""
MaskaStorage — Prompt Builder Stub
=====================================
Constructs structured prompts for the LLM from a user query and
retrieved document context chunks.

TODO: Implement prompt templates and context formatting.
"""

from app.utils.logger import get_logger

logger = get_logger(__name__)

# ─── System prompt template ───────────────────────────────────────────────────
SYSTEM_PROMPT_TEMPLATE = """You are a helpful AI assistant with access to a document archive.
Answer the user's question using ONLY the information provided in the context below.
If the context does not contain enough information to answer, say so clearly.
Do not make up information.

Context:
{context}
"""


class PromptBuilder:
    """
    Builds structured LLM prompts from query + retrieved context chunks.

    TODO: Implement the following:
    - Context window management (truncation when context exceeds token limit)
    - Source citation formatting
    - Few-shot example injection
    - Multi-turn conversation history support
    """

    def build(self, query: str, context_chunks: list[dict]) -> tuple[str, str]:
        """
        Construct a (system_prompt, user_message) pair for the LLM.

        TODO: Implement context truncation and formatting.

        Args:
            query: The user's natural-language query.
            context_chunks: List of retrieved chunk dicts (with ``text`` field).

        Returns:
            Tuple of (system_prompt, user_message) strings.

        Raises:
            NotImplementedError: Until implementation is complete.
        """
        logger.debug(
            "build() called with %d context chunks (stub — not implemented)",
            len(context_chunks),
        )
        raise NotImplementedError("PromptBuilder.build() is not yet implemented.")
