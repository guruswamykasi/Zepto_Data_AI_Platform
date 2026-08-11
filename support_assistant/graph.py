from typing import TypedDict
from langgraph.graph import StateGraph, START, END


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


class GraphState(TypedDict):
    query: str
    intent: str
    answer: str
    sources: list[str]
    confidence: float

def classify_intent(state: GraphState):

    query = state["query"].lower()

    for keyword in POLICY_KEYWORDS:

        if keyword in query:
            return {
                "intent": "policy_question"
            }

    return {
        "intent": "general_question"
    }


def retrieve_and_answer(state: GraphState):

    return {
        "answer": "Based on the retrieved context: Zepto policy information.",
        "sources": ["doc_01"],
        "confidence": 1.0
    }


def direct_answer(state: GraphState):

    return {
        "answer": "I can only answer questions about Zepto policies right now.",
        "sources": [],
        "confidence": 1.0
    }


def route_query(state: GraphState):

    if state["intent"] == "policy_question":
        return "retrieve_and_answer"

    return "direct_answer"


builder = StateGraph(GraphState)


builder.add_node(
    "classify_intent",
    classify_intent
)

builder.add_node(
    "retrieve_and_answer",
    retrieve_and_answer
)

builder.add_node(
    "direct_answer",
    direct_answer
)


builder.add_edge(
    START,
    "classify_intent"
)


builder.add_conditional_edges(
    "classify_intent",
    route_query,
    {
        "retrieve_and_answer": "retrieve_and_answer",
        "direct_answer": "direct_answer"
    }
)


builder.add_edge(
    "retrieve_and_answer",
    END
)

builder.add_edge(
    "direct_answer",
    END
)


graph = builder.compile()


if __name__ == "__main__":

    policy_query = {
        "query": "How long does delivery take?",
        "intent": "",
        "answer": "",
        "sources": [],
        "confidence": 0.0
    }

    result = graph.invoke(policy_query)

    print("POLICY QUESTION")
    print(result)


    general_query = {
        "query": "Who is the president of India?",
        "intent": "",
        "answer": "",
        "sources": [],
        "confidence": 0.0
    }

    result = graph.invoke(general_query)

    print()
    print("GENERAL QUESTION")
    print(result)