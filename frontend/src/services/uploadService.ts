/**
 * MaskaStorage — Upload Service
 * ================================
 * Handles all API calls related to document uploading.
 *
 * TODO: Add progress tracking via onUploadProgress callback.
 */

import apiClient from "./apiClient";
import type { UploadResponse } from "../types";

/**
 * Upload a document file to the backend.
 *
 * @param file - The File object to upload.
 * @param tags - Optional tags to associate with the document.
 * @param description - Optional description.
 * @returns The upload acknowledgement response.
 */
export async function uploadDocument(
  file: File,
  tags: string[] = [],
  description?: string,
): Promise<UploadResponse> {
  // TODO: Add upload progress callback support
  const formData = new FormData();
  formData.append("file", file);

  const response = await apiClient.post<UploadResponse>("/upload", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });

  return response.data;
}
