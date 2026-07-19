from services.llm import LLMService  # adjust import if needed

llm=LLMService()

for chunk in llm.stream("Explain Spring Boot in 100 words."):
    print(chunk.content, end="", flush=True)