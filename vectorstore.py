from langchain_chroma import Chroma

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from app.config import VECTORSTORE_PATH


EMBEDDING_MODEL = (
    "sentence-transformers/all-MiniLM-L6-v2"
)


def get_embeddings():

    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )


def create_vectorstore(
    documents
):

    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=VECTORSTORE_PATH
    )

    return vectorstore


def load_vectorstore():

    embeddings = get_embeddings()

    return Chroma(
        persist_directory=VECTORSTORE_PATH,
        embedding_function=embeddings
    )


def search_documents(
    query: str,
    k: int = 5
):

    vectorstore = load_vectorstore()

    results = vectorstore.similarity_search(
        query,
        k=k
    )

    return results