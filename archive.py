import streamlit as st 
import requests
from exception.exceptions import TradingBotException
import sys
BASE_URL = "http://localhost:8003"

st.set_page_config(
    page_title="Stock Market Multi-Agent Chatbot",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("📈 Stock Market Agentic Chatbot")


with st.sidebar:
    st.header("📄 Upload Documents")
    st.markdown("Upload your **stock market related PDF or DOCX files** to prepare the knowledge base.")
    uploaded_files = st.file_uploader("Choose files", type=["pdf", "docx"], accept_multiple_files=True)
    print(uploaded_files)


    if st.button("Upload and Ingest" ):
        if uploaded_files:
            files = []
            for f in uploaded_files:
                file_data = f.read()
                if not file_data:
                    continue
                files.append(("files",(getattr(f, "name", "file.pdf"), file_data,f"type")))


            if files:
                try:
                    with st.spinner("Uploading and processing files..."):
                        response = requests.post(f"{BASE_URL}/upload",files=files)

                        if response.status_code == 200:
                            st.success("✅ Files uploaded and processed successfully!")


                        else:
                            st.error("❌ Upload failed: " + response.text)

                except Exception as e:
                    raise TradingBotException(e, sys)
                else:
                    st.warning("Some files are empty or unreadable.")




# Main Panel: Ask a Question
st.header("🤖 Ask a Question")
st.markdown("Enter your **stock market related** question. The Chatbot will search the documents and respond intelligently.")


question = st.text_input("Your question", placeholder="e.g. What are the financials of Apple Inc.?")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            payload = {"question": question}
            response = requests.post(f"{BASE_URL}/query", json=payload)

            if response.status_code == 200:
                answer = response.json().get("answer", "No answer found.")
                st.markdown("🤖 Answer: " + answer)
                st.write(answer)
            else:
                st.error("❌ An error occurred: " + response.text)