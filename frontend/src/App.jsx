import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'
import ArchivePage from './pages/ArchivePage'
import ChatPage from './pages/ChatPage'
import { UploadPage } from './pages/UploadPage'
import './App.css'

// Provisional routing shell for local page testing.
// This is a temporary setup and should be reviewed by Priyanshu/Pranav before merging.
export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/upload" element={<UploadPage />} />
        <Route path="/archive" element={<ArchivePage />} />
        <Route path="/chat" element={<ChatPage />} />
        <Route path="/*" element={<Navigate to="/upload" replace />} />
      </Routes>
    </BrowserRouter>
  )
}
