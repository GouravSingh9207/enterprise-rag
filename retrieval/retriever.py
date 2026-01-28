from dotenv import load_dotenv
load_dotenv()

from langchain_core.vectorstores import VectorStoreRetriever
from retrieval.load_db import load_vectordb


def get_retriever(top_k: int = 4):
    vectordb = load_vectordb()

    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": top_k},
    )

    return retriever


if __name__ == "__main__":
    retriever = get_retriever()
    docs = retriever.invoke("What is Gourav's current role?")
    print(f"Retrieved {len(docs)} chunks")
    print(docs[0].page_content[:300])
