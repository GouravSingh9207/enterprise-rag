from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv(dotenv_path=".env")  # 👈 force load

print("API key found:", os.getenv("OPENAI_API_KEY") is not None)

llm = ChatOpenAI(model="gpt-4o-mini")
print(llm.invoke("Say hello in one sentence"))
