import { useEffect, useRef, useState } from 'react'
import ReactMarkdown from 'react-markdown'
import { useChatStream } from '../hooks/useChatStream'
import './ChatPage.css'

// TODO(Priyanshu): swap for the shared Chip component once the UI library lands
function SourceChips({ sources }) {
  if (!sources || sources.length === 0) return null

  return (
    <div className="chat-sources">
      {sources.map((source) => (
        <a
          key={source.id}
          className="chat-source-chip"
          href={source.sourceUrl}
          target="_blank"
          rel="noreferrer"
        >
          <span className="chat-source-type">{source.sourceType}</span>
          {source.title}
        </a>
      ))}
    </div>
  )
}

function ChatBubble({ message }) {
  const isUser = message.role === 'user'

  return (
    <div className={`chat-row ${isUser ? 'chat-row--user' : 'chat-row--assistant'}`}>
      <div className={`chat-bubble ${isUser ? 'chat-bubble--user' : 'chat-bubble--assistant'}`}>
        {isUser ? (
          <p className="chat-bubble-text">{message.content}</p>
        ) : (
          <>
            <div className="chat-markdown">
              <ReactMarkdown>{message.content}</ReactMarkdown>
            </div>
            {message.isStreaming && <span className="chat-cursor" aria-hidden="true" />}
            {!message.isStreaming && <SourceChips sources={message.sources} />}
          </>
        )}
      </div>
    </div>
  )
}

export default function ChatPage() {
  const { messages, sendMessage, isStreaming } = useChatStream()
  const [draft, setDraft] = useState('')
  const scrollAnchorRef = useRef(null)

  useEffect(() => {
    scrollAnchorRef.current?.scrollIntoView({ behavior: 'smooth', block: 'end' })
  }, [messages])

  const handleSubmit = (event) => {
    event.preventDefault()
    if (!draft.trim() || isStreaming) return
    sendMessage(draft)
    setDraft('')
  }

  return (
    <div className="chat-page">
      <div className="chat-scroll">
        {messages.length === 0 ? (
          <div className="chat-empty">
            <h2>Ask anything about your saved documents</h2>
            <p>Answers are grounded in the URLs and PDFs you've uploaded to your archive.</p>
          </div>
        ) : (
          messages.map((message) => <ChatBubble key={message.id} message={message} />)
        )}
        <div ref={scrollAnchorRef} />
      </div>

      {/* TODO(Priyanshu): swap this raw form markup for the shared Input + Button components once the UI library lands */}
      <form className="chat-input-bar" onSubmit={handleSubmit}>
        <input
          className="chat-input"
          type="text"
          value={draft}
          onChange={(event) => setDraft(event.target.value)}
          placeholder="Ask a follow-up question..."
          disabled={isStreaming}
          aria-label="Chat message"
        />
        <button
          type="submit"
          className="chat-send-button"
          disabled={isStreaming || !draft.trim()}
        >
          {isStreaming ? 'Thinking…' : 'Send'}
        </button>
      </form>
    </div>
  )
}
