# MaskaStorage — API Contract

## Base URL

| Environment | URL |
|---|---|
| Development | `http://localhost:8000/api/v1` |
| Production | `https://api.maskaStorage.example.com/api/v1` |

---

## Authentication

> **TODO**: Authentication is not yet implemented. All endpoints are currently open.
> Plan: API key via `X-API-Key` header, with JWT for user sessions.

---

## Response Format

All responses use JSON. Error responses follow a consistent schema:

```json
{
  "error": true,
  "status_code": 422,
  "detail": "filename: field required",
  "path": "/api/v1/upload"
}
```

---

## Endpoints

### Health

#### `GET /health`

Returns the liveness status of the API server.

**Response 200:**
```json
{
  "status": "ok"
}
```

---

### Upload

#### `POST /upload`

Upload a document for processing.

**Request:** `multipart/form-data`

| Field | Type | Required | Description |
|---|---|---|---|
| `file` | `File` | Yes | The document file |

**Response 202:**
```json
{
  "status": "accepted",
  "filename": "report.pdf",
  "message": "File accepted for processing.",
  "document_id": "d290f1ee-6c54-4b01-90e6-d701748f0851"
}
```

**Error Responses:**
- `413` — File exceeds size limit
- `415` — File type not supported

---

### Archive

#### `GET /archive`

Retrieve a paginated list of all archived documents.

**Query Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `page` | `int` | `1` | Page number (1-indexed) |
| `page_size` | `int` | `20` | Items per page (max 100) |

**Response 200:**
```json
{
  "items": [
    {
      "document_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
      "filename": "report.pdf",
      "file_type": "pdf",
      "size_bytes": 204800,
      "status": "ready",
      "tags": ["research"],
      "description": "Q4 Financial Report",
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-15T10:31:00Z",
      "metadata": {}
    }
  ],
  "total": 1,
  "page": 1,
  "page_size": 20
}
```

---

#### `GET /archive/{document_id}`

Retrieve a single archived document.

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `document_id` | `string (UUID)` | Document identifier |

**Response 200:** Returns a single `ArchiveItem` object.

**Error Responses:**
- `404` — Document not found

---

#### `DELETE /archive/{document_id}`

Delete an archived document.

**Response 202:**
```json
{
  "document_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
  "message": "Document deletion — not yet implemented."
}
```

---

### Chat

#### `POST /chat`

Send a natural-language query and receive an AI-generated answer.

**Request Body:**
```json
{
  "query": "What are the key findings in the Q4 report?",
  "top_k": 5,
  "include_sources": true
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `query` | `string` | Yes | User query (1–2000 chars) |
| `top_k` | `int` | No | Max source chunks (1–20, default 5) |
| `include_sources` | `bool` | No | Include source citations (default true) |

**Response 200:**
```json
{
  "answer": "The key findings indicate...",
  "query": "What are the key findings in the Q4 report?",
  "sources": [
    {
      "document_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
      "filename": "q4_report.pdf",
      "excerpt": "Revenue grew by 23% YoY...",
      "relevance_score": 0.92
    }
  ],
  "model": "gpt-4o"
}
```
