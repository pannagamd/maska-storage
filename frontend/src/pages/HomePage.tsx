/**
 * MaskaStorage — Home Page (Placeholder)
 * =========================================
 * Minimal placeholder confirming the frontend scaffold is operational.
 * Replace with real UI when the Home feature is implemented.
 */

import React from "react";
import { APP_NAME, APP_VERSION } from "../constants";

/**
 * Placeholder home page rendered at the "/" route.
 */
export function HomePage(): React.JSX.Element {
  return (
    <section className="home-page" aria-labelledby="home-heading">
      <div className="home-page__badge">✅ Frontend Running</div>

      <h1 id="home-heading" className="home-page__title">
        Welcome to <span className="home-page__brand">{APP_NAME}</span>
      </h1>

      <p className="home-page__subtitle">
        AI-powered document storage &amp; retrieval
      </p>

      <div className="home-page__status-card" role="status" aria-live="polite">
        <h2 className="home-page__status-title">Scaffold Status</h2>
        <ul className="home-page__status-list">
          <li>
            <span className="home-page__check">✓</span> React{" "}
            <strong>18</strong> + Vite + TypeScript
          </li>
          <li>
            <span className="home-page__check">✓</span> React Router v6
            configured
          </li>
          <li>
            <span className="home-page__check">✓</span> Existing{" "}
            <code>src/</code> architecture preserved
          </li>
          <li>
            <span className="home-page__check">✓</span> Services, hooks,
            constants &amp; types intact
          </li>
          <li>
            <span className="home-page__check">✓</span>{" "}
            <code>npm run dev</code> successful
          </li>
        </ul>
      </div>

      <p className="home-page__version">v{APP_VERSION}</p>
    </section>
  );
}

export default HomePage;
