from services.rag.loader import DocumentLoader
from services.rag.splitter import DocumentSplitter
from services.rag.vector_store import VectorStore
from services.rag.retriever import Retriever

class RAGService:

    def __init__(self):
        self.loader=DocumentLoader()
        self.splitter=DocumentSplitter()
        self.vector_store=VectorStore()

        self.db=None
        self.retriever=None
    
    def ingest(self,folder_path):
        documents=self.loader.load(folder_path)

        chunks=self.splitter.split(documents=documents)

        self.db = self.vector_store.create(chunks)

        self.db.save_local("data/faiss_index")

        self.retriever=Retriever(self.db)

    def load_vector_store(self):

        self.db=self.vector_store.load("data/faiss_index")

        self.retriever=Retriever(self.db)

    def retrieve(self,question):

        results= self.retriever.retrieve(question=question)

        documents=[]
        scores=[]

        for doc,score in results:
            documents.append(doc)
            scores.append(score)
        
        return documents,scores


