import uuid
import logging

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.agent.graph import build_graph
from app.agent.checkpointer import create_checkpointer

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/sessions", tags=["sessions"])

_graph = None
_checkpointer = None


async def _get_graph():
    global _graph, _checkpointer
    if _graph is None:
        _checkpointer = await create_checkpointer()
        _graph = build_graph(checkpointer=_checkpointer)
        logger.info("Planning graph initialised")
    return _graph


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)
    session_id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="Send the same ID to continue a conversation; omit to start new.",
    )


class ChatResponse(BaseModel):
    session_id: str
    reply: str


class SessionState(BaseModel):
    session_id: str
    message_count: int
    next_node: list[str] | None = None


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    graph = await _get_graph()
    thread_config = {"configurable": {"thread_id": request.session_id}}

    try:
        result = await graph.ainvoke(
            {"messages": [{"role": "user", "content": request.message}]},
            config=thread_config,
        )
    except Exception as e:
        logger.exception("Graph execution failed for session %s", request.session_id)
        raise HTTPException(status_code=500, detail=f"Agent error: {e}")

    messages = result.get("messages", [])
    assistant_messages = [
        m for m in messages
        if (hasattr(m, "type") and m.type == "ai")
        or (isinstance(m, dict) and m.get("role") == "assistant")
    ]

    if not assistant_messages:
        raise HTTPException(status_code=500, detail="Agent produced no response")

    last = assistant_messages[-1]
    reply = last.content if hasattr(last, "content") else last.get("content", "")
    return ChatResponse(session_id=request.session_id, reply=reply)


@router.get("/{session_id}", response_model=SessionState)
async def get_session(session_id: str):
    graph = await _get_graph()
    thread_config = {"configurable": {"thread_id": session_id}}

    try:
        state = await graph.aget_state(thread_config)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Session {session_id} not found")

    if not state or not state.values:
        raise HTTPException(status_code=404, detail=f"Session {session_id} not found")

    messages = state.values.get("messages", [])
    next_nodes = list(state.next) if state.next else None
    return SessionState(
        session_id=session_id,
        message_count=len(messages),
        next_node=next_nodes,
    )