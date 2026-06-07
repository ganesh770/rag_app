from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents(path):
    loader=PyPDFLoader(path)
    documents = loader.load()
    splitter= RecursiveCharacterTextSplitter(chunk_size = 500,chunk_overlap=100)
    chunks=splitter.split_documents(documents)
    print("documents has been loaded successfully")
    return chunks 

if __name__=="__main__":
    print(load_documents(r"C:\flutter_projects\rag_app\data\sample.pdf"))
    
