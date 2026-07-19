"""
MaskaStorage — Application Constants
======================================
Static values that never change at runtime.
Keep all magic strings and numbers here — never hard-code them inline.
"""

# ─── Application ─────────────────────────────────────────────────────────────
APP_TITLE = "MaskaStorage API"
APP_DESCRIPTION = "AI-powered document storage, retrieval, and chat backend."
API_V1_PREFIX = "/api/v1"

# ─── Allowed file types ──────────────────────────────────────────────────────
ALLOWED_FILE_EXTENSIONS: set[str] = {"pdf", "docx", "txt", "md", "html"}

# ─── File size limits ────────────────────────────────────────────────────────
MAX_UPLOAD_SIZE_MB = 50
MAX_UPLOAD_SIZE_BYTES = MAX_UPLOAD_SIZE_MB * 1024 * 1024  # 52 428 800 bytes

# ─── Pagination defaults ─────────────────────────────────────────────────────
DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# ─── Chunking / Embeddings ───────────────────────────────────────────────────
DEFAULT_CHUNK_SIZE = 512       # tokens per chunk
DEFAULT_CHUNK_OVERLAP = 64     # overlap between consecutive chunks
EMBEDDING_DIMENSIONS = 1536    # dimensions for text-embedding-3-small

# ─── Vector Store ────────────────────────────────────────────────────────────
VECTOR_STORE_COLLECTION = "maska_documents"
TOP_K_RESULTS = 5              # default number of retrieval results

# ─── Response messages ───────────────────────────────────────────────────────
MSG_HEALTH_OK = "ok"
MSG_UPLOAD_ACCEPTED = "File accepted for processing."
MSG_NOT_FOUND = "The requested resource was not found."
MSG_INTERNAL_ERROR = "An unexpected internal error occurred."

# ─── HTTP Headers ────────────────────────────────────────────────────────────
HEADER_REQUEST_ID = "X-Request-ID"
HEADER_PROCESS_TIME = "X-Process-Time"
