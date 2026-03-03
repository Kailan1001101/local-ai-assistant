from app.embeddings.embedder import embed_one, embed_many
from app.retrieval.simple_retriever import retrieve_top_k

chunks = [
    "Employees get 15 days annual leave",
    "Contractors receive 10 days leave",
    "The office closes at 5pm"
]

chunk_vectors = embed_many(chunks)

question = "How many leave days do contractors get?"

question_vector = embed_one(question)

results = retrieve_top_k(question_vector, chunks, chunk_vectors, k=2)

print(results)