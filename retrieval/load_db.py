from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


def load_vectordb(
    persist_dir: str = "data/chroma",
    collection_name: str = "enterprise_rag",
):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    vectordb = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=persist_dir,
    )

    return vectordb


if __name__ == "__main__":
    db = load_vectordb()
    print("Vector DB loaded")
