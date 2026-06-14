import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.set_page_config(
    page_title="Research Paper Reasoning Assistant",
    layout="wide"
)

st.title("📚 Research Paper Reasoning Assistant")
st.write("Upload research papers and ask citation-grounded questions.")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Upload Paper")

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file is not None:
        if st.button("Upload and Ingest"):
            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            with st.spinner("Uploading and indexing paper..."):
                response = requests.post(f"{API_URL}/upload", files=files)

            if response.status_code == 200:
                result = response.json()
                st.success(
                    f"📄 {result['file_name']} uploaded and indexed successfully."
                )
            else:
                st.error("Upload failed.")
                st.write(response.text)

    st.divider()

    st.subheader("Uploaded Papers")
    st.caption(
        "Uploaded papers will be used as the knowledge base for answering questions."
    )

with col2:
    st.subheader("Ask a Question")

    question = st.text_input(
        "Enter your question",
        placeholder="Example: What is self-attention?"
    )

    if st.button("Ask"):
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Retrieving relevant sources and generating answer..."):
                response = requests.post(
                    f"{API_URL}/ask",
                    json={"question": question}
                )

            if response.status_code == 200:
                result = response.json()

                st.subheader("Answer")
                with st.container(border=True):
                    st.write(result["answer"])

                st.subheader("Sources")
                if result["sources"]:
                    for source in result["sources"]:
                        st.info(
                            f"📄 **{source['file_name']}**  \n"
                            f"Similarity Score: `{source['score']}`"
                        )
                else:
                    st.warning("No strong sources found.")
            else:
                st.error("Question failed.")
                st.write(response.text)