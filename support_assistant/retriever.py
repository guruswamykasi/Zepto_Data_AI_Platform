from vector_store import search_documents


def retrieve_and_answer(query):

    results = search_documents(query, top_k=3)

    if not results:
        return {
            "answer": "No relevant policy information was found.",
            "sources": [],
            "confidence": 0.0
        }

    top_chunk = results[0]

    snippet = top_chunk["content"][:200]

    return {
        "answer": f"Based on the retrieved context: {snippet}",
        "sources": [
            result["id"]
            for result in results
        ],
        "confidence": 1.0
    }