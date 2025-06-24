# LLM-Security Labs

Hands-on notebooks that accompany the **LLM Security Notebook**.

| Lab | Colab | Local Folder |
|-----|-------|--------------|
| Prompt Injection | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/codemedici/llm-security-labs/blob/main/prompt_injection_lab/prompt_injection_lab.ipynb) | `prompt_injection_lab/` |
| Pickle Backdoor | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/codemedici/llm-security-labs/blob/main/pickle_backdoor_lab/pickle_backdoor_lab.ipynb) | `pickle_backdoor_lab/` |
| Firewall Bypass | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/codemedici/llm-security-labs/blob/main/firewall_bypass_lab/firewall_bypass_lab.ipynb) | `firewall_bypass_lab/` |
| Vector DB Poison | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/codemedici/llm-security-labs/blob/main/vector_poison_lab/vector_poison_lab.ipynb) | `vector_poison_lab/` |

## Prerequisites

- Python 3.10+  
- Docker & Docker-Compose (for vector-poison lab)  
- OpenAI API key (`export OPENAI_API_KEY=...`)  
- Optional: Lakera API key (`LAKERA_API_KEY`) & Azure Content-Safety keys

Clone and run notebooks locally (`jupyter lab`) or click the **“Open in Colab”** badge inside each `.ipynb`.

> **Security Note**  
> Labs are intentionally vulnerable. Run in an isolated environment or container.
