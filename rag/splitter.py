from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

class DocumentSplitter :
    """Splits Documents into smaller chunks for embeddings"""

    def __init__(self , chunk_size : int = 600 , chunk_overlap : int = 60) :

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size = chunk_size,
            chunk_overlap = chunk_overlap
        )
    
    def split(self , docs: list[Document]) -> list[Document] :
        return self.splitter.split_documents(docs)