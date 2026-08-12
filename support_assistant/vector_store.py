import chromadb
from sentence_transformers import SentenceTransformer

from chucker import create_chunks
from embedding_store import create_embedding_model

MODEL_NAME = "all-MiniLM-L6-v2"
DB_PATH = "chroma_db"
COLLECTION_NAME = "zepto_policies"


client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_collection(
    name="zepto_policies"
)

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

def search_documents(query, top_k=3):

    query_embedding = create_embedding_model().encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results["documents"][0]
    ids = results["ids"][0]

    results_list = []

    for document_id, content in zip(ids, documents):

        results_list.append({
            "id": document_id,
            "content": content
        })

    return results_list