/**
 * MaskaStorage — Frontend Constants
 * ====================================
 * Application-wide constants for the frontend.
 * Values that change per environment must use VITE_ env vars instead.
 */

// ─── API ─────────────────────────────────────────────────────────────────────

/** Base URL of the backend API — set via VITE_API_BASE_URL env var. */
export const API_BASE_URL: string =
  import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

/** API version prefix. */
export const API_VERSION: string = import.meta.env.VITE_API_VERSION ?? "v1";

/** Full API prefix: e.g., http://localhost:8000/api/v1 */
export const API_PREFIX: string = `${API_BASE_URL}/api/${API_VERSION}`;

/** Default request timeout in milliseconds. */
export const API_TIMEOUT_MS: number = Number(import.meta.env.VITE_API_TIMEOUT_MS) || 30_000;

// ─── Upload ──────────────────────────────────────────────────────────────────

/** Maximum allowed file upload size in bytes (default 50 MB). */
export const MAX_UPLOAD_SIZE_BYTES: number =
  (Number(import.meta.env.VITE_MAX_UPLOAD_SIZE_MB) || 50) * 1024 * 1024;

/** Allowed file MIME types for the file picker. */
export const ALLOWED_MIME_TYPES: string[] = [
  "application/pdf",
  "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
  "text/plain",
  "text/markdown",
  "text/html",
];

// ─── Pagination ───────────────────────────────────────────────────────────────

export const DEFAULT_PAGE = 1;
export const DEFAULT_PAGE_SIZE = 20;

// ─── App ─────────────────────────────────────────────────────────────────────

export const APP_NAME: string = import.meta.env.VITE_APP_NAME ?? "MaskaStorage";
export const APP_VERSION: string = import.meta.env.VITE_APP_VERSION ?? "0.1.0";

// ─── Document Statuses ────────────────────────────────────────────────────────

export const DOCUMENT_STATUS_LABELS: Record<string, string> = {
  pending: "Pending",
  processing: "Processing",
  ready: "Ready",
  failed: "Failed",
} as const;
