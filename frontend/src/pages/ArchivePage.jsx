import { useState } from 'react'
import { useArchive } from '../hooks/useArchive'

// NOTE: Tailwind may not be configured yet in this repo.
// The className values here are placeholders and should be updated to real Tailwind utilities once Tailwind is installed.
export default function ArchivePage() {
    const { items, isLoading, error, filterItems } = useArchive()
    const [query, setQuery] = useState('')
    const [expandedId, setExpandedId] = useState(null)

    const handleFilterChange = (event) => {
        const nextQuery = event.target.value
        setQuery(nextQuery)
        filterItems(nextQuery)
    }

    const toggleCard = (id) => {
        setExpandedId((current) => (current === id ? null : id))
    }

    return (
        <div className="archive-page-container p-6 max-w-6xl mx-auto">
            <div className="archive-header mb-6">
                <h1 className="text-3xl font-semibold mb-2">Archive</h1>
                <p className="text-base text-slate-600">
                    Browse your saved documents, filter by keywords, and expand cards for full details.
                </p>
            </div>

            <div className="archive-filter mb-6">
                {/* TODO: Priyanshu component */}
                <input
                    type="search"
                    value={query}
                    onChange={handleFilterChange}
                    placeholder="Search titles, summaries, or key points"
                    className="w-full border rounded px-4 py-3"
                    aria-label="Filter archive items"
                />
            </div>

            {isLoading ? (
                <div className="archive-empty py-12 text-center text-slate-600">Loading archive items…</div>
            ) : error ? (
                <div className="archive-empty py-12 text-center text-red-600">{error}</div>
            ) : items.length === 0 ? (
                <div className="archive-empty py-12 text-center text-slate-600">
                    No saved items match your query yet. Try a broader search or upload a document first.
                </div>
            ) : (
                <div className="archive-grid grid gap-6 sm:grid-cols-2 xl:grid-cols-3">
                    {items.map((item) => {
                        const isExpanded = expandedId === item.id
                        return (
                            <div
                                key={item.id}
                                className="archive-card border rounded-lg p-5 bg-white shadow-sm cursor-pointer"
                                onClick={() => toggleCard(item.id)}
                            >
                                {/* TODO: Priyanshu component */}
                                <div className="card-header mb-3 flex items-center justify-between gap-3">
                                    <div>
                                        <p className="text-sm text-slate-500 mb-1">{item.sourceType.toUpperCase()}</p>
                                        <h2 className="text-xl font-semibold">{item.title}</h2>
                                    </div>
                                    <span className="badge rounded-full px-3 py-1 text-xs uppercase tracking-wide bg-slate-100 text-slate-700">
                                        {item.sourceType}
                                    </span>
                                </div>

                                <p className="text-slate-700 line-clamp-3">{item.summary}</p>

                                {isExpanded ? (
                                    <div className="card-expanded mt-4 space-y-4">
                                        <div>
                                            <p className="text-sm text-slate-500">Source URL</p>
                                            <a
                                                className="text-blue-600 underline break-all"
                                                href={item.sourceUrl}
                                                target="_blank"
                                                rel="noreferrer"
                                                onClick={(event) => event.stopPropagation()}
                                            >
                                                {item.sourceUrl}
                                            </a>
                                        </div>
                                        <div>
                                            <p className="text-sm text-slate-500 mb-2">Key points</p>
                                            <ul className="list-disc list-inside text-slate-700 space-y-1">
                                                {item.keyPoints.map((point, index) => (
                                                    <li key={index}>{point}</li>
                                                ))}
                                            </ul>
                                        </div>
                                        <p className="text-sm text-slate-500">Saved at {new Date(item.savedAt).toLocaleString()}</p>
                                    </div>
                                ) : (
                                    <div className="card-footer mt-4 text-sm text-slate-500">Click to expand for full details</div>
                                )}
                            </div>
                        )
                    })}
                </div>
            )}
        </div>
    )
}
