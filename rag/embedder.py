from langchain_huggingface import HuggingFaceEmbeddings
from core.config import get_settings

settings = get_settings()

class EmbedderModel:
    '''
    Loads and provides access to the HuggingFace embedding model.
    '''
    _embedder = None

    @staticmethod
    def get_embedder():
        if EmbedderModel._embedder is None:
            EmbedderModel._embedder = HuggingFaceEmbeddings(model_name=settings.HUGGINGFACE_EMBEDDING_MODEL)
        return EmbedderModel._embedder