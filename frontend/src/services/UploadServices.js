import apiClient from "./apiClient";

// Upload a URL
export async function uploadUrl(url) {
  const response = await apiClient.post("/upload/url", { url });
  return response.data;
}

// Upload a PDF file
export async function uploadPdf(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await apiClient.post("/upload/pdf", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return response.data;
}