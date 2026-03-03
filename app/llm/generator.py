from app.utils.logger import log
import requests

LLM_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

def generate_answer(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    log("LLM", "Sending prompt to LLM")
    response = requests.post(LLM_URL, json=payload)

    result = response.json()["response"]
    log("LLM", "LLM response received")
    return result