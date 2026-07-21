import { simulateUploadProcess } from '../mocks/mockUploadData'

const USE_MOCKS = import.meta.env.VITE_USE_MOCKS === 'true'

export async function uploadUrl(url) {
  if (USE_MOCKS) {
    return simulateUploadProcess(url)
  }

  // Real mode placeholder contract:
  // POST /api/upload with { url }
  // Expected response: { title, summary, keyPoints }
  const res = await fetch('/api/upload', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ url }),
  })

  if (!res.ok) {
    throw new Error(`URL upload failed with status ${res.status}`)
  }

  return res.json()
}

export async function uploadFile(file) {
  if (USE_MOCKS) {
    return simulateUploadProcess(file)
  }

  const formData = new FormData()
  if (file instanceof File) {
    formData.append('file', file)
  } else {
    formData.append('file', file)
  }

  // Real mode placeholder contract:
  // POST /api/upload with multipart/form-data containing file
  // Expected response: { title, summary, keyPoints }
  const res = await fetch('/api/upload', {
    method: 'POST',
    body: formData,
  })

  if (!res.ok) {
    throw new Error(`File upload failed with status ${res.status}`)
  }

  return res.json()
}
