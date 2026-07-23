import { useState } from "react";
import { useUpload } from "../hooks/useUpload";

export default function UploadPage() {
  const [url, setUrl] = useState("");
  const { loading, error, result, submitUrl, submitPdf } = useUpload();

  function handleUrlSubmit(e) {
    e.preventDefault();
    if (url.trim()) submitUrl(url.trim());
  }

  function handleFileChange(e) {
    const file = e.target.files[0];
    if (file) submitPdf(file);
  }

  return (
    <div className="max-w-xl mx-auto p-6">
      <h1 className="text-2xl font-semibold mb-4">Upload Content</h1>

      <form onSubmit={handleUrlSubmit} className="flex gap-2 mb-4">
        <input
          type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Paste a URL"
          className="flex-1 border rounded px-3 py-2"
        />
        <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">
          Submit
        </button>
      </form>

      <input type="file" accept="application/pdf" onChange={handleFileChange} />

      {loading && <p className="mt-4 text-gray-500">Uploading...</p>}
      {error && <p className="mt-4 text-red-600">{error}</p>}
      {result && <p className="mt-4 text-green-600">Uploaded successfully.</p>}
    </div>
  );
}