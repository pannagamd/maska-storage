/**
 * MaskaStorage — Frontend Utilities
 * =====================================
 * Pure utility functions shared across the frontend application.
 * No side effects, no API calls, no React hooks.
 */

import { MAX_UPLOAD_SIZE_BYTES, ALLOWED_MIME_TYPES } from "../constants";

// ─── File Utilities ───────────────────────────────────────────────────────────

/**
 * Format a file size in bytes into a human-readable string.
 *
 * @param bytes - File size in bytes.
 * @returns Formatted string e.g. "1.2 MB", "456 KB".
 */
export function formatFileSize(bytes: number): string {
  if (bytes === 0) return "0 B";
  const units = ["B", "KB", "MB", "GB"];
  const i = Math.floor(Math.log(bytes) / Math.log(1024));
  return `${(bytes / Math.pow(1024, i)).toFixed(1)} ${units[i]}`;
}

/**
 * Check whether a file passes size and type validation rules.
 *
 * @param file - The File object to validate.
 * @returns Object with `valid` boolean and optional `error` message.
 */
export function validateFile(file: File): { valid: boolean; error?: string } {
  if (file.size > MAX_UPLOAD_SIZE_BYTES) {
    return {
      valid: false,
      error: `File exceeds the maximum allowed size (${formatFileSize(MAX_UPLOAD_SIZE_BYTES)}).`,
    };
  }
  if (!ALLOWED_MIME_TYPES.includes(file.type)) {
    return {
      valid: false,
      error: `File type "${file.type}" is not supported.`,
    };
  }
  return { valid: true };
}

// ─── Date / Time Utilities ────────────────────────────────────────────────────

/**
 * Format an ISO-8601 UTC string into a localised date string.
 *
 * @param isoString - ISO-8601 date string from the API.
 * @param locale - BCP 47 language tag (default: browser locale).
 * @returns Human-readable date string.
 */
export function formatDate(isoString: string, locale?: string): string {
  try {
    return new Date(isoString).toLocaleDateString(locale, {
      year: "numeric",
      month: "short",
      day: "numeric",
    });
  } catch {
    return isoString;
  }
}

// ─── String Utilities ─────────────────────────────────────────────────────────

/**
 * Truncate a string to `maxLength` characters, appending an ellipsis.
 *
 * @param text - The string to truncate.
 * @param maxLength - Maximum character length.
 * @returns Truncated string.
 */
export function truncate(text: string, maxLength: number = 100): string {
  if (text.length <= maxLength) return text;
  return `${text.slice(0, maxLength - 1)}…`;
}

/**
 * Convert a camelCase or snake_case string to Title Case.
 *
 * @param str - Input string.
 * @returns Title-cased string.
 */
export function toTitleCase(str: string): string {
  return str
    .replace(/_/g, " ")
    .replace(/([A-Z])/g, " $1")
    .replace(/\s+/g, " ")
    .trim()
    .replace(/\b\w/g, (c) => c.toUpperCase());
}

// ─── Object Utilities ─────────────────────────────────────────────────────────

/**
 * Remove keys with `undefined` or `null` values from an object.
 *
 * @param obj - The input object.
 * @returns A new object without null/undefined entries.
 */
export function omitNullish<T extends Record<string, unknown>>(obj: T): Partial<T> {
  return Object.fromEntries(
    Object.entries(obj).filter(([, v]) => v !== undefined && v !== null),
  ) as Partial<T>;
}
