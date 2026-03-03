from app.embeddings.embedder import embed_one

text = "Employees get 15 days annual leave"

vector = embed_one(text)

print(len(vector))