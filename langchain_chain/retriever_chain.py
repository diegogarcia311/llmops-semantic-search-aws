from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader

# Load docs (mock)
loader = TextLoader("data/docs.txt")
documents = loader.load()

# Embedding + Vector Store
embedding = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embedding)

# Retrieval QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

query = "Summarize the underwriting guidelines."
result = qa_chain.run(query)
print(result)
