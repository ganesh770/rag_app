from app.rag.embedder import load_vector_store

def get_retriever():
    db = load_vector_store()
    retriever = db.as_retriever(search_kwargs={'k':3})
    return retriever 