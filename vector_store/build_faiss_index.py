from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader

# Load data and create FAISS index
loader = TextLoader("data/policies.txt")
docs = loader.load()
embedding = OpenAIEmbeddings()
faiss_index = FAISS.from_documents(docs, embedding)

# Save locally
faiss_index.save_local("faiss_index")
