import json
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Load FAISS index
index = FAISS.load_local("faiss_index", OpenAIEmbeddings())
qa = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=index.as_retriever())

def lambda_handler(event, context):
    query = event.get("queryStringParameters", {}).get("q", "")
    result = qa.run(query)
    return {
        "statusCode": 200,
        "body": json.dumps({"response": result})
    }
