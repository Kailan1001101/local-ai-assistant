from app.embeddings.embedder import embed_many, embed_one
from app.retrieval.simple_retriever import retrieve_top_k
from app.context.context_builder import build_context
from app.llm.generator import generate_answer

# Knowledge base
chunks = [
    "All employees get a car allowance benefit.",
    "The company provides pension fund benefits.",
    "Interest rates are currently low.",
    "Employees receive 8 days of leave annually."
]

# Embed knowledge
chunk_vectors = embed_many(chunks)

# User question
question = "How many leave days do employees get?"

# Embed question
question_vector = embed_one(question)

# Retrieve top 2 relevant chunks
retrieved = retrieve_top_k(question_vector, chunks, chunk_vectors, k=2)

# Build context prompt
prompt = build_context(question, retrieved)

# Generate answer from LLM
answer = generate_answer(prompt)

from app.evaluation.evaluator import evaluate_answer

answer = generate_answer(prompt)

print(answer)

evaluate_answer(answer, retrieved)
