from document_loader import load_documents


def create_chunks(documents):

    chunks = []

    for document in documents:

        chunk = {
            "chunk_id": document["id"] + "_chunk_01",
            "document_id": document["id"],
            "content": document["content"]
        }

        chunks.append(chunk)

    return chunks


if __name__ == "__main__":

    documents = load_documents()

    chunks = create_chunks(documents)

    print("Number of documents:", len(documents))
    print("Number of chunks:", len(chunks))

    for chunk in chunks:

        print("\n--------------------")
        print("Chunk ID:", chunk["chunk_id"])
        print("Document ID:", chunk["document_id"])
        print("Content:", chunk["content"][:150])

