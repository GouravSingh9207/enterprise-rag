import streamlit as st
import requests

st.set_page_config(page_title="Enterprise RAG", layout="centered")

st.title("📄 Enterprise RAG Assistant")
st.caption("Ask questions grounded in your documents")

API_URL = "http://127.0.0.1:8000/query"

question = st.text_input(
    "Ask a question",
    placeholder="Summarize Gourav's leadership experience",
)

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            response = requests.post(
                API_URL,
                json={"question": question},
                timeout=60,
            )

        if response.status_code == 200:
            data = response.json()

            st.subheader("Answer")
            st.write(data["answer"])

            st.subheader("Sources")
            for src in data["sources"]:
                st.write(f"- {src}")

            st.caption(f"Latency: {data['latency_ms']} ms")
        else:
            st.error("API error occurred")
