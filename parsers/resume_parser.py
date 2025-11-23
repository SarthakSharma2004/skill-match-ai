from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader
import os

class ResumeParser :
    '''Auto Detects PDF or Docx and extracts clean text'''


    def parse(self , file_path: str) -> str :
        ext = os.path.splitext(file_path)[1].lower()

        if ext == '.pdf' :
            return self.extract_pdf(file_path)
        
        elif ext == '.docx' :
            return self.extract_docx(file_path)
        
        else :
            raise ValueError(f'Unsupported file format: {ext}')
        
    
    def extract_pdf(self , file_path: str) -> str :
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        return docs

    def extract_docx(self , file_path: str) -> str :
        loader = Docx2txtLoader(file_path)
        docs = loader.load()
        return docs

