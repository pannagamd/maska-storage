import { mockArchiveItems } from '../mocks/mockArchiveData'

const USE_MOCKS = import.meta.env.VITE_USE_MOCKS === 'true'

export async function getItems() {
  if (USE_MOCKS) {
    // Simulate realistic async network delay
    await new Promise((resolve) => setTimeout(resolve, 300))
    return mockArchiveItems
  }

  // Real mode placeholder contract:
  // GET /api/archive
  // Expected response: [{ id, title, summary, sourceType, sourceUrl, savedAt, keyPoints }, ...]
  const res = await fetch('/api/archive', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  })

  if (!res.ok) {
    throw new Error(`Failed to fetch archive items: ${res.status}`)
  }

  return res.json()
}
