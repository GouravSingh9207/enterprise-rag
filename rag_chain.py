from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from retrieval.retriever import get_retriever
from prompts.rag_prompt import RAG_PROMPT


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

retriever = get_retriever(top_k=4)

rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough(),
    }
    | RAG_PROMPT
    | llm
    | StrOutputParser()
)


if __name__ == "__main__":
    answer = rag_chain.invoke(
        "Summarize Gourav's leadership and data engineering experience."
    )
    print(answer)
