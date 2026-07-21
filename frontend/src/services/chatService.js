import { mockChatAnswerChunks, mockChatSources } from '../mocks/mockChatData'

const USE_MOCKS = import.meta.env.VITE_USE_MOCKS === 'true'

export async function sendMessage(question) {
  if (USE_MOCKS) {
    // Simulate initial latency before returning answer chunks and sources
    await new Promise((resolve) => setTimeout(resolve, 400))
    return {
      answerChunks: mockChatAnswerChunks,
      sources: mockChatSources,
    }
  }

  // Real mode placeholder contract:
  // POST /api/chat with { question }
  // Expected response: { answerChunks: string[], sources: [{ id, title, sourceType, sourceUrl }] }
  const res = await fetch('/api/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ question }),
  })

  if (!res.ok) {
    throw new Error(`Chat request failed with status ${res.status}`)
  }

  return res.json()
}
