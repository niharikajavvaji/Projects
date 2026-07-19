from typing import TypedDict

class AgentState(TypedDict):
    question:str
    documents:list
    answer:str
    route:str
    scores:list[float]
    history:list
    tool_result:str
   