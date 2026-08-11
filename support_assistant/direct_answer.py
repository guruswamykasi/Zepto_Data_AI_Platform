def direct_answer(state):

    return {
        "answer":
            "I can only answer questions about Zepto policies right now.",
        "sources": [],
        "confidence": 1.0
    }


if __name__ == "__main__":

    state = {
        "query": "Who is Virat Kohli?"
    }

    result = direct_answer(state)

    print(result)