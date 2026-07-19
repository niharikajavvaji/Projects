import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    
    def __init__(self):
        self.groq_api_key=os.getenv("GROQ_API_KEY")
        self.model="openai/gpt-oss-120b"
        self.temperature=0


    DOCUMENTS_PATH = "data"
    DB_PATH = "data/faiss_index"


settings=Settings()