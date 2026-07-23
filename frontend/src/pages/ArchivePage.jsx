import { useArchive } from "../hooks/useArchive";

export default function ArchivePage() {
  const { items, loading, error, removeItem } = useArchive();

  if (loading) return <p className="p-6 text-gray-500">Loading archive...</p>;
  if (error) return <p className="p-6 text-red-600">{error}</p>;

  return (
    <div className="max-w-2xl mx-auto p-6">
      <h1 className="text-2xl font-semibold mb-4">Archive</h1>

      {items.length === 0 && <p className="text-gray-500">No items yet.</p>}

      <ul className="space-y-2">
        {items.map((item) => (
          <li
            key={item.id}
            className="flex justify-between items-center border rounded px-3 py-2"
          >
            <span>{item.title || item.url}</span>
            <button
              onClick={() => removeItem(item.id)}
              className="text-red-600 text-sm"
            >
              Remove
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}