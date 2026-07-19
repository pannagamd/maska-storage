/**
 * MaskaStorage — API Types
 * =========================
 * TypeScript type definitions matching the backend Pydantic schemas.
 * Keep these in sync with backend/app/schemas/*.py
 */

// ─── Health ──────────────────────────────────────────────────────────────────

export interface HealthResponse {
  status: string;
}

// ─── Upload ──────────────────────────────────────────────────────────────────

export interface UploadRequest {
  tags?: string[];
  description?: string;
}

export interface UploadResponse {
  status: string;
  filename: string;
  message: string;
  document_id: string;
}

// ─── Archive ─────────────────────────────────────────────────────────────────

export type DocumentStatus = "pending" | "processing" | "ready" | "failed";

export interface ArchiveItem {
  document_id: string;
  filename: string;
  file_type: string;
  size_bytes: number;
  status: DocumentStatus;
  tags: string[];
  description: string | null;
  created_at: string; // ISO-8601 UTC string
  updated_at: string; // ISO-8601 UTC string
  metadata: Record<string, unknown>;
}

export interface ArchiveResponse {
  items: ArchiveItem[];
  total: number;
  page: number;
  page_size: number;
  message?: string | null;
}

// ─── Chat ─────────────────────────────────────────────────────────────────────

export interface SourceDocument {
  document_id: string;
  filename: string;
  excerpt: string;
  relevance_score: number;
}

export interface ChatRequest {
  query: string;
  top_k?: number;
  include_sources?: boolean;
}

export interface ChatResponse {
  answer: string;
  query: string;
  sources: SourceDocument[];
  model: string;
}

// ─── Shared / Utility ────────────────────────────────────────────────────────

export interface ApiError {
  error: boolean;
  status_code: number;
  detail: string;
  path: string;
}

export interface PaginationParams {
  page: number;
  page_size: number;
}
