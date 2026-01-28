from dotenv import load_dotenv
load_dotenv()  

from pathlib import Path
from langchain_core.documents import Document
from pypdf import PdfReader


def load_pdfs(data_dir: str) -> list[Document]:
    docs = []
    data_path = Path(data_dir)

    for pdf_path in data_path.glob("*.pdf"):
        reader = PdfReader(pdf_path)
        full_text = []

        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text.append(text)

        content = "\n".join(full_text)

        docs.append(
            Document(
                page_content=content,
                metadata={
                    "source": pdf_path.name,
                    "doc_type": "pdf",
                },
            )
        )

    return docs


if __name__ == "__main__":
    documents = load_pdfs("data")
    print(f"Loaded {len(documents)} documents")
