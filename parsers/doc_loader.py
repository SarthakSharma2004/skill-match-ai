from langchain.schema import Document
from langchain.document_loaders import PyPDFLoader , Docx2txtLoader
from pathlib import Path

class DocumentLoader:
    ''' 
    Utility class for loading and parsing documents into LangChain Document objects.
    Supports PDF and DOCX formats and returns a list of Document objects
    '''

    @staticmethod
    def load(file_path: str) -> list[Document] :
        ext = Path(file_path).suffix.lower()

        if ext == ".pdf" :
            return DocumentLoader.extract_pdf(file_path)
        
        elif ext == ".docx" :
            return DocumentLoader.extract_docx(file_path)

        else :
            raise ValueError(f"Unsupported file type: {ext}")
        
        
    @staticmethod
    def extract_pdf(file_path: str) -> list[Document] :
        loader = PyPDFLoader(file_path)
        return loader.load()
    

    @staticmethod
    def extract_docx(file_path: str) -> list[Document] :
        loader = Docx2txtLoader(file_path)
        return loader.load()