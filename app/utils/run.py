from app.rag.loader import load_documents
from app.rag.embedder import create_vector_store


chunks = load_documents(
    r"data/sample.pdf"
)

create_vector_store(chunks)

print("Vector DB created successfully")