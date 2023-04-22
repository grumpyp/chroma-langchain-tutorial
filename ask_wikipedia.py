from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from typing import List
from langchain.schema import Document
import os


os.environ['OPENAI_API_KEY'] = "your-api-key"


class Genie:

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.loader = TextLoader(self.file_path)
        self.documents = self.loader.load()
        self.texts = self.text_split(self.documents)
        self.vectordb = self.embeddings(self.texts)
        self.genie = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=self.vectordb.as_retriever())

    @staticmethod
    def text_split(documents: TextLoader):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)
        return texts

    @staticmethod
    def embeddings(texts: List[Document]):
        embeddings = OpenAIEmbeddings()
        vectordb = Chroma.from_documents(texts, embeddings)
        return vectordb

    def ask(self, query: str):
        return self.genie.run(query)


if __name__ == "__main__":
    genie = Genie("example.txt")
    print(genie.ask("Can you tell me the formula for Linear Regression?"))