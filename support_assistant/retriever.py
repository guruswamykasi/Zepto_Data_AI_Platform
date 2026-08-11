def retrieve_and_answer(state):

    query = state["query"]

    print("Retrieving documents for:", query)

    return {
        "answer": "Based on the retrieved context: test answer",
        "sources": ["doc_01"],
        "confidence": 1.0
    }


if __name__ == "__main__":

    state = {
        "query": "What is the delivery fee?"
    }

    result = retrieve_and_answer(state)

    print(result)