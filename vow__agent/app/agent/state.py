from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class PlanningState(TypedDict):
    """Everything the agent carries as it works.
    
    Started minimal — Kareem's schema (PLN-01) will expand this
    once the joint session happens.
    """
    messages: Annotated[list, add_messages]