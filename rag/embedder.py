from core.config import get_settings
from langchain.schema import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings

settings = get_settings()


class EmbedderModel:

    @staticmethod
    def get_embedder():
        return GoogleGenerativeAIEmbeddings(
            model = "gemini-embedding-001" , 
            google_api_key = settings.GOOGLE_API_KEY
        )
