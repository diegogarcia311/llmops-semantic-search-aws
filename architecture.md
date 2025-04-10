# 🧱 Architecture – LLMOps Semantic Search on AWS

This document outlines the high-level architecture of the semantic search platform built using AWS-native services, LangChain, and FAISS.

---

## 📊 High-Level Flow

```plaintext
[User Query]
     ↓
[API Gateway]
     ↓
[AWS Lambda Function]
     ↓
[LangChain Chain]
     ↓
[FAISS Vector DB (HNSW)]
     ↓
[OpenAI LLM Completion]
     ↓
[Response to User]
