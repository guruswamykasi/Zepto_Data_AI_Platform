from fastapi import FastAPI
from pydantic import BaseModel

from graph import run_graph
from models import AnswerResponse



app = FastAPI(
    title="Zepto Support Assistant",
    description="Zepto policy question answering service",
    version="1.0.0"
)


class AskRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {
        "message": "Welcome to Zepto Support Assistant"
    }


@app.post("/ask", response_model=AnswerResponse)
def ask_question(request: AskRequest):

    result = run_graph(request.query)

    return result