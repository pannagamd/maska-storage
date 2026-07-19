/**
 * MaskaStorage — Shared Layout Component
 * =========================================
 * Provides the application shell: navigation sidebar/header + main content area.
 * No page-specific UI — structural wrapper only.
 *
 * TODO: Replace placeholder navigation items with real routes once
 *       pages are implemented.
 */

import React from "react";
import { APP_NAME } from "../constants";

interface LayoutProps {
  children: React.ReactNode;
}

/**
 * Root application layout wrapping all pages.
 *
 * @param children - The page content to render inside the layout.
 */
export function Layout({ children }: LayoutProps): React.JSX.Element {
  return (
    <div className="layout">
      {/* ── Application Header ────────────────────────────── */}
      <header className="layout__header">
        <div className="layout__logo">
          <span className="layout__logo-icon" aria-hidden="true">🗄️</span>
          <span className="layout__logo-name">{APP_NAME}</span>
        </div>
        <nav className="layout__nav" aria-label="Main navigation">
          {/* TODO: Replace with React Router <NavLink> components */}
          <a href="/" className="layout__nav-link">Home</a>
          <a href="/upload" className="layout__nav-link">Upload</a>
          <a href="/archive" className="layout__nav-link">Archive</a>
          <a href="/chat" className="layout__nav-link">Chat</a>
        </nav>
      </header>

      {/* ── Main Content ──────────────────────────────────── */}
      <main className="layout__main" role="main">
        {children}
      </main>

      {/* ── Footer ───────────────────────────────────────── */}
      <footer className="layout__footer">
        <p>© {new Date().getFullYear()} {APP_NAME}. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default Layout;
