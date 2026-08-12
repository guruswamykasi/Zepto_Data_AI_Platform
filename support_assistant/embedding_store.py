import chromadb
from sentence_transformers import SentenceTransformer

from chucker import create_chunks
from document_loader import load_documents


MODEL_NAME = "all-MiniLM-L6-v2"
COLLECTION_NAME = "zepto_policies"


def create_embedding_model():

    model = SentenceTransformer(MODEL_NAME)

    return model


def create_chroma_collection():

    client = chromadb.PersistentClient(path="chroma_db")

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={
            "description": "Zepto policy documents"
        }
    )

    return collection


def store_embeddings():

    
    documents = load_documents()

    chunks = create_chunks(documents)

    model = create_embedding_model()

    collection = create_chroma_collection()

    texts = [chunk["content"] for chunk in chunks]

    embeddings = model.encode(texts).tolist()

    ids = [chunk["chunk_id"] for chunk in chunks]

    collection.upsert(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=[
            {
                "document_id": chunk["document_id"]
            }
            for chunk in chunks
        ]
    )

    print("Embeddings stored successfully.")
    print("Number of chunks:", collection.count())

    return collection



def search_documents(query, top_k=3):

    query_embedding = model.encode(query).tolist()

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

