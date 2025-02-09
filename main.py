import os
import json
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from rag_utility import process_document_to_chroma_db, answer_question

# Define FastAPI app
app = FastAPI()

working_dir = os.getcwd()

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(working_dir, file.filename)
    
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    process_document_to_chroma_db(file.filename)
    return JSONResponse(content={"message": "Document Processed Successfully!"})

@app.post("/query/")
async def query_pdf(question: str = Form(...)):
    answer = answer_question(question)
    return JSONResponse(content={"answer": answer})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)






# import os

# import streamlit as st
# from rag_utility import process_document_to_chroma_db,answer_question


# working_dir = os.getcwd()
# st.title("🐳 deepSeek-R1- Document RAG")

# #file uploader widget
# uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# if uploaded_file is not None:
#     #define save path
#     save_path = os.path.join(working_dir,uploaded_file.name)
#     with open(save_path,"wb") as f:
#         f.write(uploaded_file.getbuffer())
#     process_doc = process_document_to_chroma_db(uploaded_file.name)
#     st.info("Document Processed Successfully")

# # Text widget to get user input
# user_question  = st.text_area("Ask your question about the document")

# if st.button("Answer"):
#     answer = answer_question(user_question)
#     st.markdown("### DeepSeek-R1")
#     st.markdown(answer)
