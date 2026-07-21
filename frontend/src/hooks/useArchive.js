import { useEffect, useState } from 'react'
import { getItems } from '../services/archiveService'

export function useArchive() {
    const [allItems, setAllItems] = useState([])
    const [items, setItems] = useState([])
    const [isLoading, setIsLoading] = useState(false)
    const [error, setError] = useState(null)

    useEffect(() => {
        async function loadItems() {
            setIsLoading(true)
            setError(null)

            try {
                const fetchedItems = await getItems()
                setAllItems(fetchedItems)
                setItems(fetchedItems)
            } catch (err) {
                setError(err.message || 'Failed to load archive items.')
            } finally {
                setIsLoading(false)
            }
        }

        loadItems()
    }, [])

    const filterItems = (query) => {
        if (!query?.trim()) {
            setItems(allItems)
            return
        }

        const normalizedQuery = query.trim().toLowerCase()
        const filtered = allItems.filter((item) => {
            const haystack = `${item.title} ${item.summary} ${item.keyPoints?.join(' ')} ${item.sourceUrl}`.toLowerCase()
            return haystack.includes(normalizedQuery)
        })

        setItems(filtered)
    }

    return { items, isLoading, error, filterItems }
}
