import { useCallback, useRef, useState } from 'react'
import { sendMessage as sendChatMessage } from '../services/chatService'

const STREAM_CHUNK_DELAY_MS = 45

let messageIdCounter = 0
function nextMessageId() {
  messageIdCounter += 1
  return `msg-${messageIdCounter}`
}

export function useChatStream() {
  const [messages, setMessages] = useState([])
  const [isStreaming, setIsStreaming] = useState(false)
  // Tracks the in-flight stream so a superseded call can't keep writing to state.
  const activeStreamRef = useRef(0)

  const sendMessage = useCallback(async (question) => {
    const trimmedQuestion = question.trim()
    if (!trimmedQuestion || isStreaming) return

    const assistantId = nextMessageId()
    const userMessage = { id: nextMessageId(), role: 'user', content: trimmedQuestion }
    const assistantMessage = {
      id: assistantId,
      role: 'assistant',
      content: '',
      sources: [],
      isStreaming: true,
      error: false,
    }

    setMessages((prev) => [...prev, userMessage, assistantMessage])
    setIsStreaming(true)

    const streamId = ++activeStreamRef.current

    const patchAssistantMessage = (patch) => {
      setMessages((prev) =>
        prev.map((message) =>
          message.id === assistantId ? { ...message, ...patch } : message
        )
      )
    }

    try {
      const { answerChunks, sources } = await sendChatMessage(trimmedQuestion)

      for (const chunk of answerChunks) {
        if (activeStreamRef.current !== streamId) return
        await new Promise((resolve) => setTimeout(resolve, STREAM_CHUNK_DELAY_MS))
        setMessages((prev) =>
          prev.map((message) =>
            message.id === assistantId
              ? { ...message, content: message.content + chunk }
              : message
          )
        )
      }

      if (activeStreamRef.current !== streamId) return
      patchAssistantMessage({ sources: sources || [], isStreaming: false })
    } catch {
      if (activeStreamRef.current !== streamId) return
      patchAssistantMessage({
        content: 'Something went wrong while generating a response. Please try again.',
        isStreaming: false,
        error: true,
      })
    } finally {
      if (activeStreamRef.current === streamId) {
        setIsStreaming(false)
      }
    }
  }, [isStreaming])

  return { messages, sendMessage, isStreaming }
}
