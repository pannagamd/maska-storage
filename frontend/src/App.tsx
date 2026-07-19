/**
 * MaskaStorage — Application Root
 * ==================================
 * Sets up React Router and renders the top-level layout.
 * Page implementations will be added here as features are built out.
 */

import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { Layout } from "./components/Layout";
import { HomePage } from "./pages/HomePage";

function App(): React.JSX.Element {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          {/* Home — placeholder confirmation page */}
          <Route path="/" element={<HomePage />} />

          {/* Future pages — uncomment as implemented */}
          {/* <Route path="/upload"  element={<UploadPage />} /> */}
          {/* <Route path="/archive" element={<ArchivePage />} /> */}
          {/* <Route path="/chat"    element={<ChatPage />} /> */}

          {/* Fallback: redirect unknown paths to home */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}

export default App;
