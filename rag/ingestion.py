from pathlib import Path

from langchain_community.document_loaders import (
    PyMuPDFLoader
)


def load_documents(
    directory: str
):

    documents = []

    directory_path = Path(directory)

    pdf_files = list(
        directory_path.glob("*.pdf")
    )

    for pdf_file in pdf_files:

        loader = PyMuPDFLoader(
            str(pdf_file)
        )

        docs = loader.load()

        documents.extend(docs)

    return documents

print("done")