from dotenv import load_dotenv
load_dotenv()

import time
from fastapi import FastAPI

from api.schemas import QueryRequest, QueryResponse
from api.logger import setup_logger
from rag_chain import rag_chain
from retrieval.retriever import get_retriever

app = FastAPI(
    title="Enterprise RAG API",
    version="1.0.0",
)

logger = setup_logger()
retriever = get_retriever(top_k=4)


@app.post("/query", response_model=QueryResponse)
def query_rag(request: QueryRequest):
    start = time.time()

    # Retrieve documents explicitly for logging
    docs = retriever.invoke(request.question)
    sources = list({doc.metadata.get("source") for doc in docs})

    answer = rag_chain.invoke(request.question)

    latency = round((time.time() - start) * 1000, 2)

    logger.info(
        f"question='{request.question}' | "
        f"sources={sources} | "
        f"latency_ms={latency}"
    )

    return QueryResponse(
        answer=answer,
        sources=sources,
        latency_ms=latency,
    )
