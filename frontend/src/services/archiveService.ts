/**
 * MaskaStorage — Archive Service
 * ================================
 * Handles all API calls related to the document archive.
 */

import apiClient from "./apiClient";
import type { ArchiveItem, ArchiveResponse, PaginationParams } from "../types";

/**
 * Fetch a paginated list of all archived documents.
 *
 * @param params - Pagination parameters.
 * @returns Paginated archive response.
 */
export async function listArchive(
  params: PaginationParams = { page: 1, page_size: 20 },
): Promise<ArchiveResponse> {
  const response = await apiClient.get<ArchiveResponse>("/archive", { params });
  return response.data;
}

/**
 * Fetch a single archived document by ID.
 *
 * @param documentId - Unique document identifier.
 * @returns The archive item.
 */
export async function getArchiveItem(documentId: string): Promise<ArchiveItem> {
  const response = await apiClient.get<ArchiveItem>(`/archive/${documentId}`);
  return response.data;
}

/**
 * Delete an archived document by ID.
 *
 * @param documentId - Unique document identifier.
 * @returns Deletion acknowledgement.
 */
export async function deleteArchiveItem(documentId: string): Promise<{ message: string }> {
  const response = await apiClient.delete<{ message: string }>(`/archive/${documentId}`);
  return response.data;
}
