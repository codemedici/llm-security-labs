# LLM-Security Labs

Hands-on notebooks that accompany the **LLM Security Notebook**.

| Lab | Focus | Runtime |
|-----|-------|---------|
| Prompt Injection Lab | Exploit & patch direct jailbreak | Colab / Local |
| Pickle Backdoor Lab | Malicious PyTorch weights | Colab / Local |
| Firewall Bypass Lab | Evaluate Lakera & Prompt Shield | Colab / Local |
| Vector DB Poison Lab | Poison pgvector RAG pipeline | Docker Compose |

## Prerequisites

- Python 3.10+  
- Docker & Docker-Compose (for vector-poison lab)  
- OpenAI API key (`export OPENAI_API_KEY=...`)  
- Optional: Lakera API key (`LAKERA_API_KEY`) & Azure Content-Safety keys

Clone and run notebooks locally (`jupyter lab`) or click the **“Open in Colab”** badge inside each `.ipynb`.

> **Security Note**  
> Labs are intentionally vulnerable. Run in an isolated environment or container.
