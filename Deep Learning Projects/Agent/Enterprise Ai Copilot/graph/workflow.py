from langgraph.graph import StateGraph,START,END
from graph.tools import calculator_node, web_search_node,tool_answer_node

from graph.state import AgentState
from graph.nodes import retrieve_node
from graph.nodes import answer_node
from graph.nodes import chat_node
from graph.nodes import planner_node
from graph.router import router


graph = StateGraph(AgentState)

# Nodes
graph.add_node("planner", planner_node)
graph.add_node("retrieve", retrieve_node)
graph.add_node("answer", answer_node)
graph.add_node("chat", chat_node)

graph.add_node("calculator", calculator_node)
graph.add_node("web_search", web_search_node)
graph.add_node("tool_answer", tool_answer_node)

# Start
graph.add_edge(START, "planner")

# Conditional Routing
graph.add_conditional_edges(
    "planner",
    router,
    {
        "chat": "chat",
        "rag": "retrieve",
        "calculator": "calculator",
        "web_search": "web_search",
    },
)

# RAG Flow
graph.add_edge("retrieve", "answer")
graph.add_edge("answer", END)

# Chat Flow
graph.add_edge("chat", END)

# Tool Flow
graph.add_edge("calculator", "tool_answer")
graph.add_edge("web_search", "tool_answer")
graph.add_edge("tool_answer", END)

workflow = graph.compile()