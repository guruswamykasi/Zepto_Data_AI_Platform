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

