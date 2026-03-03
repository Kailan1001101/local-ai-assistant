from app.utils.logger import log

def evaluate_answer(answer, retrieved_chunks):

    top_chunk_text = retrieved_chunks[0][0]

    if answer.lower() in top_chunk_text.lower():
        log("EVAL", "Answer appears grounded in top chunk")
    else:
        log("EVAL", "WARNING: Answer may not be grounded in retrieved context")