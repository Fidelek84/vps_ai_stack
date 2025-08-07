# VPS_AI_Stack

Self-hosted AI Package is an open-source Docker Compose template that quickly sets up a robust local AI and low-code environment. It integrates Ollama for local LLMs, Open WebUI for chatting with n8n agents, and Supabase for database, vector storage, and authentication. Cole's enhanced version adds Flowise, Neo4j, Langfuse, SearXNG, and Caddy, plus preloaded RAG AI Agent workflows in n8n.


### What’s included

1. n8n              - Low-code platform 
2. Supabase         - Open source database as a service most widely used database for AI agents
3. Ollama           - Cross-platform LLM platform to install and run the latest local LLMs
4. Open WebUI       - Generative AI front end interface
5. Qdrant           - Open source, high performance vector database 
6. SearXNG          - Open source, free internet metasearch engine


## Prerequisites

Before you begin, make sure you have the following software installed:

- Python
- Git/GitHub
- Docker/Docker


## Clone

Clone the repository and navigate to the project directory:
```bash
git clone -b stable git@github.com:Fidelek84/VPS_AI_Stack.git
cd VPS_AI_Stack
```


1. Make a copy of `.env.example` and rename it to `.env` in the root directory of the project
2. Set the following required environment variables:
   ```bash
   ############
   # N8N Configuration
   ############
   N8N_ENCRYPTION_KEY=
   N8N_USER_MANAGEMENT_JWT_SECRET=

   ############
   # Supabase Secrets
   ############
   POSTGRES_PASSWORD=
   JWT_SECRET=
   ANON_KEY=
   SERVICE_ROLE_KEY=
   DASHBOARD_USERNAME=
   DASHBOARD_PASSWORD=
   POOLER_TENANT_ID=

   ############
   # Neo4j Secrets
   ############   
   NEO4J_AUTH=

   ############
   # Langfuse credentials
   ############

   CLICKHOUSE_PASSWORD=
   MINIO_ROOT_PASSWORD=
   LANGFUSE_SALT=
   NEXTAUTH_SECRET=
   ENCRYPTION_KEY=  
   ```


3. Set the following environment variables if deploying to production, otherwise leave commented:
   ```bash
   ############
   # Caddy Config
   ############

   N8N_HOSTNAME=n8n.yourdomain.com
   WEBUI_HOSTNAME=:openwebui.yourdomain.com
   SUPABASE_HOSTNAME=:supabase.yourdomain.com
   OLLAMA_HOSTNAME=:ollama.yourdomain.com
   SEARXNG_HOSTNAME=searxng.yourdomain.com
   ```  


## Deploying to the Cloud

### Prerequisites for the below steps

- Linux machine (preferably Unbuntu) with Nano, Git, and Docker installed

### Container Start

cd VPS_AI_Stack

docker-compose.yml up -d

docker ps


### Usefull Documentation

https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/
https://docs.openwebui.com/
https://supabase.com/docs
https://docs.searxng.org/
https://ollama.com/
https://qdrant.tech/documentation/