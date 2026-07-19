/**
 * MaskaStorage — useArchive Hook
 * =================================
 * Custom React hook for fetching and managing the document archive.
 *
 * TODO: Add filtering and search support.
 */

import { useState, useEffect, useCallback } from "react";
import { listArchive, deleteArchiveItem } from "../services/archiveService";
import type { ArchiveItem } from "../types";

interface UseArchiveState {
  items: ArchiveItem[];
  total: number;
  isLoading: boolean;
  error: string | null;
}

interface UseArchiveReturn extends UseArchiveState {
  refresh: () => Promise<void>;
  remove: (documentId: string) => Promise<void>;
  page: number;
  pageSize: number;
  setPage: (page: number) => void;
}

/**
 * Hook for fetching and managing the document archive.
 *
 * @param initialPage - Starting page number (default: 1).
 * @param initialPageSize - Items per page (default: 20).
 * @returns Archive state and actions.
 */
export function useArchive(initialPage = 1, initialPageSize = 20): UseArchiveReturn {
  const [page, setPage] = useState(initialPage);
  const [pageSize] = useState(initialPageSize);
  const [state, setState] = useState<UseArchiveState>({
    items: [],
    total: 0,
    isLoading: false,
    error: null,
  });

  const fetchArchive = useCallback(async () => {
    setState((prev) => ({ ...prev, isLoading: true, error: null }));
    try {
      const data = await listArchive({ page, page_size: pageSize });
      setState({ items: data.items, total: data.total, isLoading: false, error: null });
    } catch (err: unknown) {
      const message = err instanceof Error ? err.message : "Failed to load archive.";
      setState((prev) => ({ ...prev, isLoading: false, error: message }));
    }
  }, [page, pageSize]);

  useEffect(() => {
    void fetchArchive();
  }, [fetchArchive]);

  const remove = useCallback(
    async (documentId: string) => {
      try {
        await deleteArchiveItem(documentId);
        await fetchArchive();
      } catch (err: unknown) {
        const message = err instanceof Error ? err.message : "Failed to delete document.";
        setState((prev) => ({ ...prev, error: message }));
      }
    },
    [fetchArchive],
  );

  return { ...state, refresh: fetchArchive, remove, page, pageSize, setPage };
}
