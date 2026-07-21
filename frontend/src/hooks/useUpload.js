import { useState } from 'react'
import { uploadUrl as apiUploadUrl, uploadFile as apiUploadFile } from '../services/uploadService'

export function useUpload() {
  const [status, setStatus] = useState('idle') // 'idle' | 'loading' | 'success' | 'error'
  const [data, setData] = useState(null)
  const [error, setError] = useState(null)

  const uploadUrl = async (url) => {
    setStatus('loading')
    setError(null)
    try {
      const result = await apiUploadUrl(url)
      setData(result)
      setStatus('success')
      return result
    } catch (err) {
      setError(err.message || 'Failed to process URL upload.')
      setStatus('error')
      throw err
    }
  }

  const uploadFile = async (file) => {
    setStatus('loading')
    setError(null)
    try {
      const result = await apiUploadFile(file)
      setData(result)
      setStatus('success')
      return result
    } catch (err) {
      setError(err.message || 'Failed to process file upload.')
      setStatus('error')
      throw err
    }
  }

  return { status, data, error, uploadUrl, uploadFile }
}
