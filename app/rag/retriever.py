from app.rag.vectorstore import vectorstore


def retrieve_documents(query: str):

    docs = vectorstore.similarity_search(
        query,
        k=3
    )

    return [
        doc.page_content
        for doc in docs
    ]