export async function simulateUploadProcess(fileOrUrlData) {
  // Simulate 1.5 second processing delay
  await new Promise((resolve) => setTimeout(resolve, 1500))

  const sourceName =
    typeof fileOrUrlData === 'string'
      ? fileOrUrlData
      : fileOrUrlData?.name || 'Uploaded Document'

  return {
    title: `Processed Analysis: ${sourceName}`,
    summary:
      'The document was successfully ingested and parsed. Key topics include transformer model architectures, vector indexing strategies, and modern frontend design token systems.',
    keyPoints: [
      'Document parsed and chunked into 12 semantic passages.',
      'Vector embeddings generated and indexed for local RAG search.',
      'Extracted key metadata including author, publication date, and topic tags.',
      'Ready for instant context-aware Q&A in the Chat workspace.',
    ],
  }
}
