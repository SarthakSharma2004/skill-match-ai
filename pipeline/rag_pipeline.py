from parsers.doc_loader import DocumentLoader
from rag.splitter import DocumentSplitter
from rag.embedder import EmbedderModel
from rag.vector_store import VectorStore
from rag.retriever import Retriever

from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate


class RagPipeline:
    def __init__(self, index_name: str = "skillmatch-index") -> None:
        self.index_name = index_name
        self.splitter = DocumentSplitter()
        self.vectorstore_builder = VectorStore(index_name=self.index_name)
        self.retriever = None
        self.vector_store = None

    # ----------------------------------------------------
    # 1. Load → Split → Index
    # ----------------------------------------------------

    def build_index(self, file_path: str):
        
        '''Load and parse document into LangChain Document objects'''
        docs = DocumentLoader.load(file_path)

        '''Split documents into smaller chunks for embeddings'''
        chunks = self.splitter.split(docs)

        '''Store embedded chunks and return vector store'''
        self.vector_store = self.vectorstore_builder.build_vector_store(chunks)

        '''Build retriever'''
        self.retriever = Retriever.get_retriever(self.vector_store)



        