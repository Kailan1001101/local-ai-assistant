def build_context(question, retrieved_chunks):

    context_text = ""

    for i, item in enumerate(retrieved_chunks):
        chunk_text = item[0]   # extract text only
        context_text += f"{i+1}. {chunk_text}\n"

    prompt = f"""
You are an assistant answering strictly from the provided context.
If the answer is not in the context, say you don't know.

Context:
{context_text}

Question:
{question}

Answer:
"""

    return prompt