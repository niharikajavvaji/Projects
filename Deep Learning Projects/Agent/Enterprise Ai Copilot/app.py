from memory.conversation import ConversationMemory
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage
from graph.workflow import workflow

memory=ConversationMemory()

print("Enterprise AI Copilot")
print("Type 'exit' to quit.\n")

while True:

    print("\n===== Conversation History =====")
    for msg in memory.get_history():
        print(type(msg).__name__, ":", msg.content)
    print("===============================\n")

    question=input("You: ")

    if question.lower()=="exit":
        print("Goodbye!")
        break


    result=workflow.invoke(
        {
            "question":question
        }
    )

    print(result["answer"])


    memory.add_message(
        HumanMessage(content=question)
    )

    memory.add_message(AIMessage(content=result["answer"]))