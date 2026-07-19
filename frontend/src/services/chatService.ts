/**
 * MaskaStorage — Chat Service
 * ==============================
 * Handles all API calls related to the RAG chat feature.
 */

import apiClient from "./apiClient";
import type { ChatRequest, ChatResponse } from "../types";

/**
 * Send a query to the RAG chat endpoint and receive an AI-generated answer.
 *
 * @param request - The chat request payload.
 * @returns The chat response with answer and optional sources.
 */
export async function sendChatQuery(request: ChatRequest): Promise<ChatResponse> {
  const response = await apiClient.post<ChatResponse>("/chat", request);
  return response.data;
}
