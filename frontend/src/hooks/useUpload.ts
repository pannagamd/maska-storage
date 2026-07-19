/**
 * MaskaStorage — useUpload Hook
 * ================================
 * Custom React hook for handling file upload state, validation, and API calls.
 *
 * TODO: Add upload progress percentage support.
 */

import { useState, useCallback } from "react";
import { uploadDocument } from "../services/uploadService";
import { validateFile } from "../utils";
import type { UploadResponse } from "../types";

interface UseUploadState {
  isLoading: boolean;
  response: UploadResponse | null;
  error: string | null;
}

interface UseUploadReturn extends UseUploadState {
  upload: (file: File, tags?: string[], description?: string) => Promise<void>;
  reset: () => void;
}

/**
 * Hook for managing file upload lifecycle.
 *
 * @returns Upload state and actions.
 *
 * @example
 * const { upload, isLoading, response, error } = useUpload();
 * await upload(selectedFile);
 */
export function useUpload(): UseUploadReturn {
  const [state, setState] = useState<UseUploadState>({
    isLoading: false,
    response: null,
    error: null,
  });

  const upload = useCallback(
    async (file: File, tags: string[] = [], description?: string) => {
      const validation = validateFile(file);
      if (!validation.valid) {
        setState((prev) => ({ ...prev, error: validation.error ?? "Invalid file." }));
        return;
      }

      setState({ isLoading: true, response: null, error: null });
      try {
        const data = await uploadDocument(file, tags, description);
        setState({ isLoading: false, response: data, error: null });
      } catch (err: unknown) {
        const message =
          err instanceof Error ? err.message : "Upload failed. Please try again.";
        setState({ isLoading: false, response: null, error: message });
      }
    },
    [],
  );

  const reset = useCallback(() => {
    setState({ isLoading: false, response: null, error: null });
  }, []);

  return { ...state, upload, reset };
}
