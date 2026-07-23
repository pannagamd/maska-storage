import { useState } from "react";
import { uploadUrl, uploadPdf } from "../services/uploadService";

export function useUpload() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);

  async function submitUrl(url) {
    setLoading(true);
    setError(null);
    try {
      const data = await uploadUrl(url);
      setResult(data);
    } catch (err) {
      setError(err.message || "Upload failed");
    } finally {
      setLoading(false);
    }
  }

  async function submitPdf(file) {
    setLoading(true);
    setError(null);
    try {
      const data = await uploadPdf(file);
      setResult(data);
    } catch (err) {
      setError(err.message || "Upload failed");
    } finally {
      setLoading(false);
    }
  }

  return { loading, error, result, submitUrl, submitPdf };
}