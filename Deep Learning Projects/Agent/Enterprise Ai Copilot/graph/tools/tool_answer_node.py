from services.llm import LLMService

def tool_answer_node(state):

    prompt = f"""
User Question:
{state["question"]}

Tool Output:
{state["tool_result"]}

Using ONLY the tool output,
answer the user's question clearly.

If the tool output is a calculation,
present it nicely.

If it is a web search,
summarize the information.

Do not invent information.
"""
    llm=LLMService()

    answer = llm.invoke_text(prompt)

    state["answer"] = answer

    return state