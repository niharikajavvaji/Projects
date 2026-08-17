from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

chat_prompt=ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant."
        ),

        MessagesPlaceholder("history"),

        (
            "human",
            "{question}"
         )
    ]
)

