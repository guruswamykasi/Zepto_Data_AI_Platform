from fastapi import FastAPI
from pydantic import BaseModel

from graph import app_graph
from models import AnswerResponse



app = FastAPI(
    title="Zepto Support Assistant",
    description="Zepto policy question answering service",
    version="1.0.0"
)


class AskRequest(BaseModel):
    query: str


@app.post("/ask", response_model=AnswerResponse)
def ask(request: AskRequest):

    result = app_graph.invoke({
        "query": request.query,
        "intent": "",
        "answer": "",
        "sources": [],
        "confidence": 0.0
    })

    return AnswerResponse(
        answer=result["answer"],
        sources=result["sources"],
        confidence=result["confidence"]
    )