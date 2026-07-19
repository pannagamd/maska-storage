/**
 * MaskaStorage — useChat Hook
 * ==============================
 * Custom React hook for managing the RAG chat session state.
 *
 * TODO: Add multi-turn conversation history.
 */

import { useState, useCallback } from "react";
import { sendChatQuery } from "../services/chatService";
import type { ChatResponse, SourceDocument } from "../types";

export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  sources?: SourceDocument[];
  timestamp: string;
}

interface UseChatState {
  messages: ChatMessage[];
  isLoading: boolean;
  error: string | null;
}

interface UseChatReturn extends UseChatState {
  sendMessage: (query: string, topK?: number) => Promise<void>;
  clearHistory: () => void;
}

/**
 * Hook for managing the chat session and message history.
 *
 * @returns Chat state and actions.
 *
 * @example
 * const { messages, sendMessage, isLoading } = useChat();
 * await sendMessage("What are the key findings?");
 */
export function useChat(): UseChatReturn {
  const [state, setState] = useState<UseChatState>({
    messages: [],
    isLoading: false,
    error: null,
  });

  const sendMessage = useCallback(async (query: string, topK = 5) => {
    const userMessage: ChatMessage = {
      id: crypto.randomUUID(),
      role: "user",
      content: query,
      timestamp: new Date().toISOString(),
    };

    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, userMessage],
      isLoading: true,
      error: null,
    }));

    try {
      const response: ChatResponse = await sendChatQuery({
        query,
        top_k: topK,
        include_sources: true,
      });

      const assistantMessage: ChatMessage = {
        id: crypto.randomUUID(),
        role: "assistant",
        content: response.answer,
        sources: response.sources,
        timestamp: new Date().toISOString(),
      };

      setState((prev) => ({
        ...prev,
        messages: [...prev.messages, assistantMessage],
        isLoading: false,
      }));
    } catch (err: unknown) {
      const message = err instanceof Error ? err.message : "Chat request failed.";
      setState((prev) => ({ ...prev, isLoading: false, error: message }));
    }
  }, []);

  const clearHistory = useCallback(() => {
    setState({ messages: [], isLoading: false, error: null });
  }, []);

  return { ...state, sendMessage, clearHistory };
}
