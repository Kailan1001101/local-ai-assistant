# The Embedder converts text into vector representations.
# A vector is a list of numbers that captures the semantic meaning of text.

from app.utils.logger import log
import requests

# Ollama Embedding API URL
OLLAMA_URL = "http://localhost:11434/api/embeddings"

# Embedding model used for converting text → vectors
MODEL_NAME = "nomic-embed-text"


# Converts a single text string into its embedding vector.
# Used for both document chunks and user questions.
def embed_one(text):
    log("EMBED", f"Embedding text of length {len(text)}")

    payload = {
        "model": MODEL_NAME,
        "prompt": text
    }

    # Send POST request to Ollama embedding endpoint
    response = requests.post(OLLAMA_URL, json=payload)

    # Extract embedding vector from JSON response
    embedding = response.json()["embedding"]

    log("EMBED", "Embedding complete")

    return embedding


# Converts a list of text chunks into a list of embedding vectors.
# This simply calls embed_one for each chunk.
def embed_many(texts):
    embedding_chunks = []

    for text in texts:
        embedding = embed_one(text)
        embedding_chunks.append(embedding)

    return embedding_chunks