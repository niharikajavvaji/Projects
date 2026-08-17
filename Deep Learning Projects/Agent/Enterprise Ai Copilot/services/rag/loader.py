from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

class DocumentLoader:

    def load(self, folder_path: str):

        all_documents = []

        for pdf_file in Path(folder_path).glob("*.pdf"):
            loader = PyMuPDFLoader(str(pdf_file))
            all_documents.extend(loader.load())

        return all_documents