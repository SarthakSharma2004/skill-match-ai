from pinecone import Pinecone , ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain.schema import Document
from core.config import get_settings
from embedder import EmbedderModel


settings = get_settings()



class VectorStore:
    '''
    Handles Pinecone initialization and vector storage.
    '''

    def __init__(self , index_name: str = "skillmatch-index") -> None :
        self.index_name = index_name
        self.embedder = EmbedderModel.get_embedder()

        # Initialize Pinecone
        self.pc = Pinecone(
            api_key = settings.PINECONE_API_KEY,
        )

        # Create index if not already exists
        existing_index = [idx['name'] for idx in self.pc.list_indexes()]
        
        if self.index_name not in existing_index:
            self.pc.create_index(
                name = self.index_name,
                dimension = 768,
                metric = "cosine",
                spec = ServerlessSpec(
                   cloud = 'aws' , 
                   region = 'us-east-1'
                )
            )


    def build_vector_store(self, docs: list[Document]) :
        '''Store embedded chunks and return vector store.'''

        try : 
            vectorstore = PineconeVectorStore.from_documents(
                index_name = self.index_name,
                embedding = self.embedder,
                documents = docs
            )
            return vectorstore
        
        except Exception as e :
            raise RuntimeError(f"Failed to build vector store: {e}")