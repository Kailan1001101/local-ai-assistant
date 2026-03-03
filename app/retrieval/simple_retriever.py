from app.utils.logger import log
from app.similarity.cosine import cosine_similarity


# Retrieves the top-K most similar chunks to the question.
# K is configurable and determines how many chunks are returned.
#
# If K is too small:
#   - Important context may be missing.
# If K is too large:
#   - Too much context may reduce answer precision.
#
# question_vector:
#   Embedding vector of the user question.
#
# chunks:
#   List of original text chunks.
#
# chunk_vectors:
#   List of embedding vectors corresponding to each chunk.
def retrieve_top_k(question_vector, chunks, chunk_vectors, k=3):

    scored_chunks = []

    log("RETRIEVE", f"Computing similarity against {len(chunks)} chunks")

    # Compare question vector against each stored chunk vector (brute-force O(N))
    for i in range(len(chunks)):
        chunk_text = chunks[i]
        chunk_vector = chunk_vectors[i]

        score = cosine_similarity(question_vector, chunk_vector)

        scored_chunks.append((chunk_text, score))

    # Sort chunks by similarity score (highest first)
    sorted_chunks = sorted(scored_chunks, key=lambda x: x[1], reverse=True)

    log("RETRIEVE", f"Top-{k} scores: {[round(x[1], 4) for x in sorted_chunks[:k]]}")

    top_scores = [x[1] for x in sorted_chunks[:k]]

    # Score gap measures separation between the top two results.
    # A larger gap suggests stronger retrieval confidence.
    if len(top_scores) > 1:
        score_gap = top_scores[0] - top_scores[1]
    else:
        score_gap = None

    # Average score helps assess overall semantic strength of retrieved results.
    average_score = sum(top_scores) / len(top_scores)

    log("EVAL", f"Score gap: {round(score_gap,4) if score_gap is not None else 'N/A'}")
    log("EVAL", f"Average top-{k} score: {round(average_score,4)}")

    return sorted_chunks[:k]