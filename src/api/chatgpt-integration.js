const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

/**
 * Chat with GPT through the backend API
 * @param {string} input - User's message
 * @param {string} guruType - Type of guru (spiritual, sloka, meditation, etc.)
 * @param {Object} userContext - Optional user context
 * @param {boolean} stream - Whether to stream the response
 * @returns {Promise} Response from GPT
 */
export async function chatWithGPT(input, guruType = 'spiritual', userContext = null, stream = false) {
  try {
    const response = await fetch(`${API_BASE_URL}/api/spiritual/guidance`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        guru_type: guruType,
        question: input,
        user_context: userContext,
        stream: stream
      })
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error communicating with ChatGPT:', error);
    throw error;
  }
}

/**
 * Get available guru types
 * @returns {Array} List of available guru types
 */
export function getAvailableGuruTypes() {
  return [
    'spiritual',
    'sloka', 
    'meditation',
    'bhakti',
    'karma',
    'yoga'
  ];
}

/**
 * Stream chat with GPT
 * @param {string} input - User's message
 * @param {string} guruType - Type of guru
 * @param {Function} onChunk - Callback for each chunk of data
 * @param {Object} userContext - Optional user context
 */
export async function streamChatWithGPT(input, guruType = 'spiritual', onChunk, userContext = null) {
  try {
    const response = await fetch(`${API_BASE_URL}/api/spiritual/guidance/stream`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        guru_type: guruType,
        question: input,
        user_context: userContext
      })
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      const chunk = decoder.decode(value);
      const lines = chunk.split('\n');

      for (const line of lines) {
        if (line.startsWith('data: ')) {
          const data = line.slice(6);
          if (data === '[DONE]') {
            return;
          }
          try {
            const parsed = JSON.parse(data);
            onChunk(parsed);
          } catch (e) {
            // Handle malformed JSON
            console.warn('Malformed JSON in stream:', data);
          }
        }
      }
    }
  } catch (error) {
    console.error('Error streaming with ChatGPT:', error);
    throw error;
  }
}
