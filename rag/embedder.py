from langchain_huggingface import HuggingFaceEmbeddings
from core.config import get_settings

settings = get_settings()

class EmbedderModel:
    '''
    Loads and provides access to the HuggingFace embedding model.
    Initialized once so embeddings can be generated efficiently.
    '''

    def __init__(self):
        self.embedder = HuggingFaceEmbeddings(
            model_name = settings.HUGGINGFACE_EMBEDDING_MODEL
        )


    
    def get_embedder(self) :
        '''
        Returns the HuggingFaceEmbeddings object
        '''

        return self.embedder