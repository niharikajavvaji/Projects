from services.rag.rag import RAGService
from config import settings

rag=RAGService()

rag.ingest(settings.DOCUMENTS_PATH)

print("Ingestion Completed")