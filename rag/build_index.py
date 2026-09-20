from app.config import DOCUMENT_PATH

from app.rag.ingestion import (
    load_documents
)

from app.rag.vectorstore import (
    create_vectorstore
)


def main():

    print(
        "Loading PDF documents..."
    )

    documents = load_documents(
        DOCUMENT_PATH
    )

    print(
        f"Loaded {len(documents)} pages."
    )

    if not documents:

        print(
            "No PDF files found."
        )

        return

    create_vectorstore(
        documents
    )

    print(
        "Vectorstore created successfully."
    )


if __name__ == "__main__":

    main()