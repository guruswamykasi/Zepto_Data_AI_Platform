from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from router import classify_intent
from retriever import retrieve_and_answer
from direct_answer import direct_answer

class SupportState(TypedDict):
    query: str
    intent: str
    answer: str
    sources: list[str]
    confidence: float


def run_graph(query):

    intent = classify_intent(query)

    if intent == "policy_question":
        return retrieve_and_answer(query)

    return direct_answer(query)



def classify_node(state: SupportState):

    intent = classify_intent(state["query"])

    return {
        "intent": intent
    }


def retrieve_node(state: SupportState):

    result = retrieve_and_answer(state["query"])

    return result


def direct_node(state: SupportState):

    result = direct_answer(state["query"])

    return result


def route_question(state: SupportState):

    if state["intent"] == "policy_question":
        return "retrieve_and_answer"

    return "direct_answer"


graph_builder = StateGraph(SupportState)

graph_builder.add_node(
    "classify_intent",
    classify_node
)

graph_builder.add_node(
    "retrieve_and_answer",
    retrieve_node
)

graph_builder.add_node(
    "direct_answer",
    direct_node
)

graph_builder.add_edge(
    START,
    "classify_intent"
)

graph_builder.add_conditional_edges(
    "classify_intent",
    route_question,
    {
        "retrieve_and_answer": "retrieve_and_answer",
        "direct_answer": "direct_answer"
    }
)

graph_builder.add_edge(
    "retrieve_and_answer",
    END
)

graph_builder.add_edge(
    "direct_answer",
    END
)

graph = graph_builder.compile()


def run_graph(query):

    initial_state = {
        "query": query,
        "intent": "",
        "answer": "",
        "sources": [],
        "confidence": 0.0
    }

    result = graph.invoke(initial_state)

    return {
        "answer": result["answer"],
        "sources": result["sources"],
        "confidence": result["confidence"]
    }