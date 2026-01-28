from dotenv import load_dotenv
load_dotenv()  

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


def chunk_documents(
    documents: list[Document],
    chunk_size: int = 800,
    chunk_overlap: int = 120,
) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""],
    )

    chunks = splitter.split_documents(documents)

    # Add chunk index metadata
    for i, doc in enumerate(chunks):
        doc.metadata["chunk_id"] = i

    return chunks


if __name__ == "__main__":
    from load_docs import load_pdfs

    docs = load_pdfs("data")
    chunks = chunk_documents(docs)
    print(f"Created {len(chunks)} chunks")
    print(chunks[0].page_content[:300])
