from langchain_groq import ChatGroq
from config import settings


class LLMService:

    def __init__(self):

        self.llm = ChatGroq(
            model=settings.model,
            api_key=settings.groq_api_key,
            temperature=settings.temperature
        )

    def invoke(self, messages):
        return self.llm.stream(messages)

    def invoke_text(self, messages):

        response = self.llm.stream(messages)

        return response.content