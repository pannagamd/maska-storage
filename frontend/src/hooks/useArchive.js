import { useState, useEffect, useCallback } from "react";
import { getArchive, deleteArchiveItem } from "../services/archiveService";

export function useArchive() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchItems = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await getArchive();
      setItems(data);
    } catch (err) {
      setError(err.message || "Failed to load archive");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchItems();
  }, [fetchItems]);

  async function removeItem(id) {
    await deleteArchiveItem(id);
    setItems((prev) => prev.filter((item) => item.id !== id));
  }

  return { items, loading, error, refetch: fetchItems, removeItem };
}