from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain_google_genai import GoogleGenerativeAIEmbeddings

def create_vectorstore():

    docs = []

    pdfs = [
        "data/medical_book.pdf",
        "data/disease_guide.pdf"
    ]

    for pdf in pdfs:

        loader = PyPDFLoader(pdf)

        docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    db.save_local("vectorstore")

    print("Vector DB Created")