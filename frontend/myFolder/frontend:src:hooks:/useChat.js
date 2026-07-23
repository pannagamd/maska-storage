import { useState } from "react";
import { sendChatMessage } from "../services/chatService";

export function useChat() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function askQuestion(question) {
    setError(null);
    setLoading(true);

    setMessages((prev) => [...prev, { role: "user", content: question }]);
    // placeholder assistant message we'll update as chunks stream in
    setMessages((prev) => [...prev, { role: "assistant", content: "" }]);

    try {
      await sendChatMessage(question, (partialText) => {
        setMessages((prev) => {
          const updated = [...prev];
          updated[updated.length - 1] = {
            role: "assistant",
            content: partialText,
          };
          return updated;
        });
      });
    } catch (err) {
      setError(err.message || "Chat failed");
    } finally {
      setLoading(false);
    }
  }

  return { messages, loading, error, askQuestion };
}