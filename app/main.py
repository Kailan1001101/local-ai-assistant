from fastapi import FastAPI
from app.core.config import config
from app.core.logger import logger

app = FastAPI()

@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {
        "status": "Local AI Assistant running",
        "environment": config["app"]["environment"]
    }
