import { useState } from 'react'
import { useUpload } from '../hooks/useUpload'

// NOTE: Tailwind may not be configured yet in this repo.
// The className values here are placeholders and should be updated to real Tailwind utilities once Tailwind is installed.
export function UploadPage() {
    const { status, data, error, uploadUrl, uploadFile } = useUpload()
    const [mode, setMode] = useState('url') // 'url' | 'file'
    const [url, setUrl] = useState('')
    const [file, setFile] = useState(null)

    const handleSubmit = async (event) => {
        event.preventDefault()
        if (mode === 'url') {
            await uploadUrl(url)
        } else {
            if (!file) return
            await uploadFile(file)
        }
    }

    return (
        <div className="upload-page-container p-6 max-w-4xl mx-auto">
            <div className="page-header mb-6">
                <h1 className="text-3xl font-semibold mb-2">Upload content</h1>
                <p className="text-base text-slate-600">
                    Add a URL or PDF and we&apos;ll ingest it so your chat workspace can answer questions from it.
                </p>
            </div>

            <div className="mode-toggle flex gap-3 mb-6">
                <button
                    type="button"
                    className={`toggle-button px-4 py-2 rounded ${mode === 'url' ? 'active' : ''}`}
                    onClick={() => setMode('url')}
                >
                    URL
                </button>
                <button
                    type="button"
                    className={`toggle-button px-4 py-2 rounded ${mode === 'file' ? 'active' : ''}`}
                    onClick={() => setMode('file')}
                >
                    PDF
                </button>
            </div>

            <form onSubmit={handleSubmit} className="upload-form space-y-4">
                {mode === 'url' ? (
                    <div className="input-group">
                        <label className="block mb-2 font-medium">Paste a URL</label>
                        {/* TODO: Priyanshu component */}
                        <input
                            type="url"
                            value={url}
                            onChange={(event) => setUrl(event.target.value)}
                            placeholder="https://example.com/article"
                            className="input-field w-full border rounded px-4 py-3"
                            required
                        />
                    </div>
                ) : (
                    <div className="input-group">
                        <label className="block mb-2 font-medium">Upload a PDF</label>
                        {/* TODO: Priyanshu component */}
                        <input
                            type="file"
                            accept="application/pdf"
                            onChange={(event) => setFile(event.target.files?.[0] || null)}
                            className="input-field w-full"
                            required
                        />
                    </div>
                )}

                <button
                    type="submit"
                    className="submit-button inline-flex items-center justify-center rounded px-6 py-3 bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50"
                    disabled={status === 'loading'}
                >
                    {status === 'loading' ? 'Reading this for you...' : 'Submit'}
                </button>

                {error ? <p className="error-text text-red-600">{error}</p> : null}
            </form>

            {status === 'success' && data ? (
                <div className="success-card mt-8 p-6 border rounded shadow-sm bg-white">
                    {/* TODO: Priyanshu component */}
                    <h2 className="text-2xl font-semibold mb-3">Upload complete</h2>
                    <p className="text-lg font-medium mb-2">{data.title}</p>
                    <p className="text-slate-700 mb-4">{data.summary}</p>
                    {data.keyPoints?.length ? (
                        <div>
                            <h3 className="font-semibold mb-2">Key points</h3>
                            <ul className="list-disc list-inside space-y-1 text-slate-700">
                                {data.keyPoints.map((point, index) => (
                                    <li key={index}>{point}</li>
                                ))}
                            </ul>
                        </div>
                    ) : null}
                </div>
            ) : null}
        </div>
    )
}
