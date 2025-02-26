import os
import json
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))

GROQ_API_KEY = config_data["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Load the embedding model
embedding = HuggingFaceEmbeddings()

# Load the LLM model
llm = ChatGroq(
     model="deepseek-r1-distill-llama-70b",
    temperature=0
)

# Directory for storing vector database
VECTOR_STORE_DIR = os.path.join(working_dir, "doc_vectorstore")
os.makedirs(VECTOR_STORE_DIR, exist_ok=True)

def process_document_to_chroma_db(file_name):
    """Processes a PDF document and stores embeddings in ChromaDB."""
    loader = UnstructuredPDFLoader(os.path.join(working_dir, file_name))
    documents = loader.load()

    # Splitting text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    # Create a Chroma vector store
    vectordb = Chroma.from_documents(
        documents=texts,
        embedding=embedding,
        persist_directory=VECTOR_STORE_DIR
    )

    vectordb.persist()  # Persist the database for later use
    return "Document indexed successfully!"

def answer_question(user_question):
    """Retrieves an answer for a given question using the RAG pipeline."""
    vectordb = Chroma(
        persist_directory=VECTOR_STORE_DIR,
        embedding_function=embedding
    )

    retriever = vectordb.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
    )

    response = qa_chain.invoke({"query": user_question})
    return response["result"]

















# import os
# import json

# from langchain_community.document_loaders import UnstructuredPDFLoader
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_chroma import Chroma
# from langchain_groq import ChatGroq
# from langchain.chains import RetrievalQA

# working_dir = os.path.dirname(os.path.abspath((__file__)))
# config_data = json.load(open(f"{working_dir}/config.json"))

# GROQ_API_KEY = config_data["GROQ_API_KEY"]
# os.environ["GROQ_API_KEY"]=GROQ_API_KEY

# # loading the embeding model
# embedding = HuggingFaceEmbeddings()

# llm = ChatGroq(
#      model="deepseek-r1-distill-llama-70b",
#     temperature=0
# )

# def process_document_to_chroma_db(file_name):
#     #load the doc using unstructured lib
#     loader = UnstructuredPDFLoader(f"{working_dir}/{file_name}")
#     documents = loader.load()
#     #splitin text
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=2000,
#         chunk_overlap=200

#     )
#     texts = text_splitter.split_documents(documents)
#     vectordb = Chroma.from_documents(
#         documents=texts,
#         embedding=embedding,
#         persist_directory=f"{working_dir}/doc_vectorstore"

#     )
#     return 0
# def answer_question(user_question):
#     vectordb = Chroma(
#         persist_directory=f"{working_dir}/doc_vectorStore",
#         embedding_function=embedding
#     )
#     retriever = vectordb.as_retriever()
#     qa_chain = RetrievalQA.from_chain_type(
#         llm = llm,
#         chain_type="stuff",
#         retriever = retriever,
#     )
#     response = qa_chain.invoke({"query":user_question})
#     answer = response["result"]
#     return answer


