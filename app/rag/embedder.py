from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import Chroma

PERSIST_DIRECTORY = "./chroma_db"

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


class LocalEmbeddingFunction:

    def embed_documents(self, texts):

        embeddings = embedding_model.encode(texts)

        return embeddings.tolist()

    def embed_query(self, text):

        embedding = embedding_model.encode(text)

        return embedding.tolist()


def create_vector_store(chunks):

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=LocalEmbeddingFunction(),
        persist_directory=PERSIST_DIRECTORY
    )

    vector_store.persist()

    return vector_store


def load_vector_store():

    db = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=LocalEmbeddingFunction()
    )

    return db