import logging
from langgraph.graph import END, START, StateGraph
from app.agent.state import PlanningState

logger = logging.getLogger(__name__)


async def greet(state: PlanningState) -> dict:
    logger.info("Node: greet")
    return {
        "messages": [
            {
                "role": "assistant",
                "content": (
                    "Hello! I am the VOW planning agent. "
                    "Tell me about the CTV campaign you would like to plan - "
                    "market, budget, duration, and who you want to reach."
                ),
            }
        ]
    }


async def echo(state: PlanningState) -> dict:
    last_message = state["messages"][-1]
    content = last_message.content if hasattr(last_message, "content") else str(last_message)
    logger.info("Node: echo - received: %s", content[:80])
    return {
        "messages": [
            {
                "role": "assistant",
                "content": f"I heard: {content}\n\n(This is a stub - real planning nodes coming in M1.)",
            }
        ]
    }


def build_graph(checkpointer=None):
    graph = StateGraph(PlanningState)
    graph.add_node("greet", greet)
    graph.add_node("echo", echo)
    graph.add_edge(START, "greet")
    graph.add_edge("greet", "echo")
    graph.add_edge("echo", END)
    return graph.compile(checkpointer=checkpointer)