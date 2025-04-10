## 🧱 AWS Infrastructure

- **ECS + Fargate**: Hosts the containerized LangChain worker responsible for document indexing and inference
- **Lambda**: Lightweight serverless function that powers the API and calls the retriever chain
- **API Gateway**: Exposes the Lambda endpoint securely to internal tools
- **FAISS (HNSW)**: Local vector store using HNSW indexing for fast approximate similarity search
- **OpenAI / LangChain**: LLM orchestration, prompt chaining, and document parsing
- **CloudWatch**: Observability and logging for ECS and Lambda

---

## 🛠️ Module Overview

- `vector_store/`: FAISS index builder using OpenAI embeddings
- `langchain_chain/`: Custom retriever chain using LangChain and OpenAI
- `lambda_api/`: Lambda handler exposed via API Gateway
- `ecs_deploy/`: Terraform scripts for ECS + networking stack
- `notebooks/`: Local testing & exploratory workflows

---

## 📌 Deployment Considerations

- Stateless architecture using Lambda enables low-maintenance scaling
- ECS containers can be scaled horizontally or replaced by GKE for high-throughput setups
- The retriever chain and vector store layers are modular and swappable
- Can integrate with OpenSearch or Pinecone for managed vector DB

---

## 🧭 Future Roadmap

- ✅ Implemented FAISS with HNSW indexing
- ⏳ Add re-ranking step using Cohere Rerank API or OpenAI rerankers
- 🔒 Add IAM/Cognito to secure the Lambda endpoint
- ☁️ Swap FAISS for OpenSearch Vector Store in high-scale deployments
- 📂 Automate document ingestion via S3 + AWS Step Functions

---
