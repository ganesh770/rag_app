from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.chain import ask_rag

router = APIRouter()


class QueryRequest(BaseModel):
    query: str


@router.post("/ask")
def ask_question(request: QueryRequest):

    answer = ask_rag(request.query)

    return {
        "question": request.query,
        "answer": answer
    }