from fastapi import APIRouter
from pydantic import BaseModel 
from app.rag.chain import build_chain 

router = APIRouter
qa_chain = build_chain()


class QueryRequest(BaseModel):
    query : str 


@router.post("/ask")
def ask_question(request:QueryRequest):
    response= qa_chain.invoke({
        "query":request.query
    })

    return {
        "question":request.query,
        "answer":response["result"]
    }

