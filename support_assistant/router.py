POLICY_KEYWORDS = [
    "delivery",
    "return",
    "refund",
    "membership",
    "tracking",
    "cancel",
    "gift card",
    "support hours"
]


def classify_intent(state):
    query = state["query"].lower()

    for keyword in POLICY_KEYWORDS:
        if keyword in query:
            return {
                "intent": "policy_question"
            }

    return {
        "intent": "general_question"
    }


if __name__ == "__main__":

    policy_state = {
        "query": "What is the delivery fee?"
    }

    result = classify_intent(policy_state)

    print(result)

    general_state = {
        "query": "Who is the president of India?"
    }

    result = classify_intent(general_state)

    print(result)