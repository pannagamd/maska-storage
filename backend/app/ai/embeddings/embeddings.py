from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:
    """
    EmbeddingGenerator

    Responsible for:
    - Loading the embedding model
    - Generating embeddings for text chunks
    - Returning structured chunk data with embeddings

    This module does NOT perform:
    - Chunking
    - Summarization
    - Metadata generation
    - Database storage
    """

    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5"):
        """
        Initializes the embedding model.

        Args:
            model_name (str): HuggingFace embedding model.
        """

        self.model = SentenceTransformer(model_name)

    def generate(self, chunks: list) -> list:
        """
        Generates embeddings for text chunks.

        Args:
            chunks (list): List of chunk dictionaries.

        Returns:
            list: Chunks with embeddings added.
        """

        try:

            if not isinstance(chunks, list):
                raise ValueError("Input must be a list of chunks.")

            if len(chunks) == 0:
                raise ValueError("Chunk list is empty.")

            result = []

            for chunk in chunks:

                if "text" not in chunk:
                    raise ValueError("Chunk missing 'text' field.")

                embedding = self.model.encode(
                    chunk["text"],
                    normalize_embeddings=True
                )

                result.append(
                    {
                        "chunk_id": chunk["chunk_id"],
                        "text": chunk["text"],
                        "length": chunk["length"],
                        "embedding": embedding.tolist()
                    }
                )

            return result

        except Exception as e:
            raise RuntimeError(f"Embedding Generation Error: {e}")