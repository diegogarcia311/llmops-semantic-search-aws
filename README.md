# 🔍 LLMOps Semantic Search on AWS

This project demonstrates a production-grade LLMOps stack for document understanding and real-time semantic search using AWS infrastructure.

---

## 🧠 Use Case

Real-time policy document classification, Q&A, and summarization using LangChain + FAISS, served through a Lambda-powered API on ECS.

---

## 🧱 Architecture

- **LLM**: OpenAI via LangChain
- **Vector DB**: FAISS (HNSW)
- **Infra**: ECS + Fargate + Lambda + API Gateway
- **Orchestration**: Terraform
- **Monitoring**: CloudWatch, Lambda logs

![Architecture](./architecture.png) <!-- Optional image if uploaded -->

---

## 🚀 API Endpoint

Send GET request:
