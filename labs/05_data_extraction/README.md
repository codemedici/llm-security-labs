---
title: Data Extraction & Inference
owasp_id: LLM-05
difficulty: Medium
category: Data Leakage
---

## Overview

This lab demonstrates how attackers can extract memorized secrets from LLMs or embedding models by carefully probing their responses.

These attacks exploit model overfitting, improper embedding filtering, or unintended memorization during training.

## Objective
Your goal is to recover a secret **flag** hidden in the model’s embedding index using semantic similarity queries.

## Instructions

This lab runs a FastAPI service that simulates an LLM-powered vector search API.

1. Start the server:
```bash
cd labs/05_data_extraction
uvicorn vuln_embed_bot:app --reload
```

2. The `/search?q=...` endpoint returns the closest string match.
3. Craft queries that retrieve the hidden flag using semantic inference.

💡 Think of synonyms, paraphrasing, and embedding leakage edge cases.

## Sample Queries

Try using hints like:
- "internal access credentials"
- "leaked secret message"
- "password string from logs"

## Colab Link

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/codemedici/llm-security-labs/blob/main/labs/05_data_extraction/data_extraction_lab.ipynb)

## Files

- `data_extraction_lab.ipynb` – semantic extraction PoC
- `vuln_embed_bot.py` – FastAPI vector search with hidden flag
- `flag.txt` – secret phrase injected into index

## Notebook Preview

```python
import requests

URL = "http://localhost:8000/search"
QUERIES = [
    "admin password string",
    "credentials leak",
    "secret company message"
]

for q in QUERIES:
    r = requests.get(URL, params={"q": q})
    print("Prompt:", q)
    print("Match:", r.json()["match"])
```

## Resources

- Carlini et al. (Extracting Training Data from LLMs)
- OWASP Top 10 for LLMs: LLM-05
- Embedding leakage taxonomy

---
