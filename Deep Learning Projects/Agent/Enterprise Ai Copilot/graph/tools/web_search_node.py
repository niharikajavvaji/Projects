from tools.web_search import web_search


def web_search_node(state):

    question = state["question"]

    result = web_search(question)

    state["tool_result"] = result

    return state