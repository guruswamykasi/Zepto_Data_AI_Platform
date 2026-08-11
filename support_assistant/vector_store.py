import chromadb
from sentence_transformers import SentenceTransformer

from chucker import create_chunks

MODEL_NAME = "all-MiniLM-L6-v2"
DB_PATH = "chroma_db"
COLLECTION_NAME = "zepto_policies"


def create_vector_store():

    print("Loading embedding model...")

    model = SentenceTransformer(MODEL_NAME)

    print("Creating ChromaDB...")

    client = chromadb.PersistentClient(path=DB_PATH)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    print("Loading chunks...")

    chunks = create_chunks()

    ids = [chunk["id"] for chunk in chunks]

    documents = [
        chunk["content"]
        for chunk in chunks
    ]

    print("Creating embeddings...")

    embeddings = model.encode(
        documents
    ).tolist()

    print("Storing embeddings...")

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )

    print("Number of chunks:", collection.count())

    return collection


if __name__ == "__main__":

    collection = create_vector_store()

    print("Vector store created successfully.")