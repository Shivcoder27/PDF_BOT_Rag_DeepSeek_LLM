import os

import streamlit as st
from rag_utility import process_document_to_chroma_db,answer_question


working_dir = os.getcwd()
st.title("🐳 deepSeek-R1- Document RAG")

#file uploader widget
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    #define save path
    save_path = os.path.join(working_dir,uploaded_file.name)
    with open(save_path,"wb") as f:
        f.write(uploaded_file.getbuffer())
    process_doc = process_document_to_chroma_db(uploaded_file.name)
    st.info("Document Processed Successfully")

# Text widget to get user input
user_question  = st.text_area("Ask your question about the docume nt")

if st.button("Answer"):
    answer = answer_question(user_question)
    st.markdown("### DeepSeek-R1")
    st.markdown(answer)
