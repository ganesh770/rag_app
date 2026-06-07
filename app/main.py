from fastapi import FastAPI 
from .utils import run
from app.rag.chain  import router
app = FastAPI()

app.include_router(router)

@app.get('/')
def home():
    return {
        "message":"rag application is running "
    }