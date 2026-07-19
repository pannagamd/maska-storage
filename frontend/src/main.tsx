/**
 * MaskaStorage — Application Entry Point
 * ========================================
 * Bootstraps the React app and mounts it to the DOM root.
 */

import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./styles/index.css";
import App from "./App";

const rootElement = document.getElementById("root");

if (!rootElement) {
  throw new Error(
    "[MaskaStorage] Root element #root not found. Check index.html.",
  );
}

createRoot(rootElement).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
