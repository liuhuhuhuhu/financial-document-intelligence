
from fastapi import FastAPI

app = FastAPI(
    title="Financial Document Intelligence API",
    description="Backend API for financial document analysis",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "Financial Document Intelligence API",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "financial-document-intelligence"
    }
