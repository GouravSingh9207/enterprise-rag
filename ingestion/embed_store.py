from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from pathlib import Path


def embed_and_store(
    chunks: list[Document],
    persist_dir: str = "data/chroma",
    collection_name: str = "enterprise_rag",
):
    Path(persist_dir).mkdir(parents=True, exist_ok=True)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    vectordb = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=persist_dir,
    )

    vectordb.add_documents(chunks)

    return vectordb


if __name__ == "__main__":
    from load_docs import load_pdfs
    from chunking import chunk_documents

    docs = load_pdfs("data")
    chunks = chunk_documents(docs)

    db = embed_and_store(chunks)
    print(f"Stored {len(chunks)} chunks in Chroma")
