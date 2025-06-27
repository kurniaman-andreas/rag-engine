import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

# Load .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def load_pdf_data(file_path):
    loader = PyMuPDFLoader(file_path=file_path)
    return loader.load()

def split_docs(documents, chunk_size=800, chunk_overlap=80):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)

def generate_and_store_vectorstore():
    embed = OpenAIEmbeddings()

    # Load PDFs
    docs1 = load_pdf_data("data/hasil_scraping_safetravel.pdf")
    docs2 = load_pdf_data("data/Buku_Panduan_Revisi_WNI2.pdf")
    all_docs = docs1 + docs2

    # Split and embed
    chunks = split_docs(all_docs)
    vectorstore = FAISS.from_documents(chunks, embed)

    # Save to disk
    vectorstore.save_local("vectorstore_openai")
    print("✅ Vectorstore berhasil dibuat dan disimpan di 'vectorstore/'")

if __name__ == "__main__":
    generate_and_store_vectorstore()
