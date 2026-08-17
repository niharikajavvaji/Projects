from tools.calculator import calculator


def calculator_node(state):

    question = state["question"]

    result = calculator.invoke(
        {"expression": question}
    )

    state["tool_result"] = result

    return state