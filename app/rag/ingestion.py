from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.rag.vectorstore import vectorstore


def ingest_documents():

    documents = []

    pdf_files = [
        "app/rag/documents/quarterly_reports.pdf",
        "app/rag/documents/finance_notes.pdf"
    ]

    for file in pdf_files:

        loader = PyPDFLoader(file)

        docs = loader.load()

        documents.extend(docs)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    vectorstore.add_documents(chunks)

    print("Documents ingested successfully")