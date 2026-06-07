from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.retriever import get_retriever

router = APIRouter()


from app.rag.retriever import get_retriever

import ollama

def ask_rag(query):

    retriever = get_retriever()

    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Answer only from the given context.

Context:
{context}

Question:
{query}
"""

    response = ollama.chat(
        model="tinyllama",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


class QueryRequest(BaseModel):
    query: str

@router.get('/load')
def Load_everything():
    return {
        "message":"everything has been loaded"
    }


@router.post("/ask")
def ask_question(request: QueryRequest):

    answer = ask_rag(request.query)

    return {
        "question": request.query,
        "answer": answer
    }