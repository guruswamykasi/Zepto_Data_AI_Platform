from typing import TypedDict

from langgraph.graph import StateGraph, END

from router import classify_intent
from retriever import retrieve_and_answer
from direct_answer import direct_answer


class GraphState(TypedDict):
    query: str
    intent: str
    answer: str
    sources: list
    confidence: float


def route_intent(state):
    return state["intent"]


workflow = StateGraph(GraphState)

workflow.add_node(
    "classify_intent",
    classify_intent
)

workflow.add_node(
    "retrieve_and_answer",
    retrieve_and_answer
)

workflow.add_node(
    "direct_answer",
    direct_answer
)

workflow.set_entry_point(
    "classify_intent"
)

workflow.add_conditional_edges(
    "classify_intent",
    route_intent,
    {
        "policy_question":
            "retrieve_and_answer",

        "general_question":
            "direct_answer"
    }
)

workflow.add_edge(
    "retrieve_and_answer",
    END
)

workflow.add_edge(
    "direct_answer",
    END
)

app_graph = workflow.compile()