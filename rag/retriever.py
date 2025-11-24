from langchain_pinecone import PineconeVectorStore

class Retriever:
    ''' 
    Creates a retriever from an existing Pinecone vector store.
    '''

    @staticmethod
    def get_retriever(vector_store: PineconeVectorStore , k : int = 5) :
        return vector_store.as_retriever(search_kwargs={"k": k})