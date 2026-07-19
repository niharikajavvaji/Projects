from langchain_community.vectorstores import FAISS

from services.rag.embeddings import EmbeddingService


class VectorStore:

    def __init__(self):
        self.embedding = EmbeddingService().get_embedding_model()

    def create(self, chunks):
        return FAISS.from_documents(
            chunks,
            self.embedding
        )
    
    def load(self,path):
        return FAISS.load_local(
            path,
            self.embedding,
            allow_dangerous_deserialization=True
        )