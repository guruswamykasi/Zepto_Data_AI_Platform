import chromadb
from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"
DB_PATH = "chroma_db"
COLLECTION_NAME = "zepto_policies"


model = SentenceTransformer(MODEL_NAME)

client = chromadb.PersistentClient(
    path=DB_PATH
)

collection = client.get_collection(
    name=COLLECTION_NAME
)


query = "How long does Zepto take to deliver?"

query_embedding = model.encode(
    [query]
).tolist()


results = collection.query(
    query_embeddings=query_embedding,
    n_results=3
)


print("Query:")
print(query)

print("\nRetrieved documents:")

for document_id, document in zip(
    results["ids"][0],
    results["documents"][0]
):
    print("\n--------------------")
    print("ID:", document_id)
    print("Content:", document[:200])