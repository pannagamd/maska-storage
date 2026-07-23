import apiClient from "./apiClient";

export async function getArchive() {
  const response = await apiClient.get("/archive");
  return response.data;
}

export async function deleteArchiveItem(id) {
  const response = await apiClient.delete(`/archive/${id}`);
  return response.data;
}