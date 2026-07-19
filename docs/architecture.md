# MaskaStorage — System Architecture

## Overview

MaskaStorage is an AI-powered document storage, retrieval, and conversational search system. It enables users to upload documents, process them through an AI pipeline, and query their contents through a Retrieval-Augmented Generation (RAG) interface.

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Client (Browser)                         │
│                  React + TypeScript Frontend                     │
└────────────────────────────┬────────────────────────────────────┘
                             │ HTTPS / REST API
┌────────────────────────────▼────────────────────────────────────┐
│                     FastAPI Backend (Python)                     │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐  │
│   │ /health  │  │ /upload  │  │ /archive │  │    /chat     │  │
│   └──────────┘  └─────┬────┘  └────┬─────┘  └──────┬───────┘  │
│                        │            │                │           │
│              ┌──────────▼────────────▼────────────▼──┐          │
│              │          Service Layer                 │          │
│              └───────┬───────────────────────────────┘          │
│                      │                                           │
│        ┌─────────────▼───────────────────┐                      │
│        │         AI Pipeline             │                      │
│        │  Scraper → Parser → Cleaner     │                      │
│        │  → Chunker → Embeddings         │                      │
│        │  → Summarizer → Metadata        │                      │
│        └─────────────┬───────────────────┘                      │
│                      │                                           │
│        ┌─────────────▼───────────────────┐                      │
│        │       Retrieval Module           │                      │
│        │  VectorStore → Retriever →       │                      │
│        │  Ranker → PromptBuilder → RAG    │                      │
│        └─────────────────────────────────┘                      │
└────────────────────────────────────────────────────────────────┘
         │                           │
┌────────▼───────┐        ┌──────────▼──────────┐
│  PostgreSQL DB │        │  ChromaDB / Pinecone │
│  (Metadata)    │        │  (Vector Store)      │
└────────────────┘        └─────────────────────┘
```

---

## Folder Structure

```
maska-storage/
├── backend/
│   ├── app/
│   │   ├── main.py                    # FastAPI app factory
│   │   ├── core/                      # Config, constants, security
│   │   ├── api/
│   │   │   ├── routes/                # health, upload, archive, chat
│   │   │   └── dependencies.py        # Shared FastAPI dependencies
│   │   ├── schemas/                   # Pydantic request/response models
│   │   ├── database/                  # SQLAlchemy base, session, models
│   │   ├── middleware/                # CORS, logging, timing, security headers
│   │   ├── exceptions/                # Custom exceptions + handlers
│   │   ├── utils/                     # Logger, helpers, validators
│   │   ├── ai/                        # AI processing pipeline
│   │   │   ├── scraper/
│   │   │   ├── parser/
│   │   │   ├── chunking/
│   │   │   ├── embeddings/
│   │   │   ├── summarizer/
│   │   │   └── metadata.py
│   │   ├── retrieval/                 # RAG retrieval pipeline
│   │   │   ├── vector_db/
│   │   │   ├── retriever/
│   │   │   ├── prompting/
│   │   │   ├── ranker.py
│   │   │   └── rag.py
│   │   ├── services/                  # Business logic layer (TODO)
│   │   └── data/                      # File storage (uploads, processed, cache)
│   ├── tests/                         # Backend tests
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── services/                  # API service layer (apiClient, services)
│   │   ├── hooks/                     # Custom React hooks
│   │   ├── types/                     # TypeScript type definitions
│   │   ├── constants/                 # App-wide constants
│   │   ├── utils/                     # Pure utility functions
│   │   ├── components/                # Shared UI components
│   │   ├── pages/                     # Page-level components (TODO)
│   │   └── assets/                    # Static assets
│   ├── Dockerfile
│   ├── nginx.conf
│   └── .env.example
│
├── deployment/
│   ├── Dockerfile                     # Backend Dockerfile
│   ├── docker-compose.yml
│   ├── docker-compose.override.yml
│   └── aws/                           # AWS deployment configs (TODO)
│
├── docs/                              # Project documentation
├── .github/                           # GitHub Actions + templates
├── pyproject.toml                     # Ruff + pytest config
├── .eslintrc.js                       # ESLint config
├── .prettierrc                        # Prettier config
└── .editorconfig                      # Editor config
```

---

## Technology Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.11+, FastAPI, Uvicorn |
| ORM | SQLAlchemy 2.0 (async) |
| Database | PostgreSQL 16 |
| Vector Store | ChromaDB (dev), Pinecone (prod) |
| LLM | OpenAI GPT-4o |
| Embeddings | OpenAI text-embedding-3-small |
| Frontend | React 18+, TypeScript, Vite |
| Containerisation | Docker, Docker Compose |
| CI | GitHub Actions |
| Linting | Ruff (Python), ESLint + Prettier (TS) |

---

## Data Flow — Document Ingestion

1. User uploads a file via `POST /api/v1/upload`
2. File is validated (type, size) and stored in `app/data/uploads/`
3. Parser extracts raw text from the file
4. Cleaner normalises the text
5. Chunker splits the text into overlapping chunks
6. EmbeddingGenerator creates a vector for each chunk
7. Chunks + vectors are upserted into the VectorStore (ChromaDB/Pinecone)
8. Summarizer generates a document summary
9. MetadataExtractor extracts structured metadata
10. Document record is saved to PostgreSQL with status = `ready`

## Data Flow — Chat / RAG

1. User sends a query via `POST /api/v1/chat`
2. Query is embedded using EmbeddingGenerator
3. Retriever performs similarity search in VectorStore (top-k results)
4. Ranker re-ranks retrieved chunks by relevance
5. PromptBuilder constructs a structured LLM prompt with context
6. LLM generates an answer grounded in the retrieved context
7. Response (answer + sources) is returned to the client

---

## Optional Future Improvements

- Authentication with JWT / OAuth2
- Background task queue (Celery / Redis)
- Streaming chat responses (SSE / WebSockets)
- Multi-modal support (images, audio)
- RBAC (Role-Based Access Control)
- Rate limiting middleware
- OpenTelemetry tracing
