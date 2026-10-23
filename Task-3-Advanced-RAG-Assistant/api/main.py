
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Advanced RAG Assistant API",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)


@app.get("/")
def home():
    return {
        "project": "Advanced RAG Assistant",
        "status": "running",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/ask")
def ask(request: QuestionRequest):
    return {
        "question": request.question,
        "answer": (
            "The API is running. Upload and index a document "
            "through the user interface to search document content."
        )
    }
