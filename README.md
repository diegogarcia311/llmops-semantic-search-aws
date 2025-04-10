# llmops-semantic-search-aws

A scalable semantic search system using LLMOps principles and AWS cloud services. This project demonstrates how to deploy a vector search pipeline powered by embeddings and LangChain on AWS infrastructure, with CI/CD and infrastructure-as-code best practices.

---

## 🧠 Use Case

Perform semantic search over unstructured documents (PDFs, web data, etc.) using vector databases and language models — ideal for internal knowledge retrieval, customer support automation, or enterprise Q&A systems.

---

## 🏗 Architecture Diagram

```text
Client → API Gateway → Lambda (LangChain Retriever) → Vector Store (FAISS)
                                     ↘
                                 S3 / External Data
Infrastructure managed with Terraform → ECS, Lambda, etc.
