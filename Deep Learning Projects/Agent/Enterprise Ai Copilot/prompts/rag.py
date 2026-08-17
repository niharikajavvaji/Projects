from langchain_core.prompts import ChatPromptTemplate

rag_prompt=ChatPromptTemplate.from_messages([
    ("system",
     """Answer ONLY from the provided content. If
     the answer is unavailable, sau "I don't know." """
     ),
     (
         "human",
         """Context: 
         {context}

        Question:
        {question}
         
         """
         
     )
])