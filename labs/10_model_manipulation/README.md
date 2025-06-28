---
title: Model Manipulation (Backdoors & Trojans)
owasp_id: LLM-10
difficulty: Hard
category: Model-level Vulnerability
---

## Overview

This lab explores **model backdoors**: malicious behaviors injected during training or fine-tuning, triggered by specific inputs.

We simulate this with a “poisoned” LLM that behaves normally — unless it receives a special token that activates the embedded payload.

## Objective
Trigger the hidden model backdoor and extract the **flag**.

## Instructions

1. Start the poisoned model bot:
```bash
cd labs/10_model_manipulation
uvicorn vuln_backdoored_bot:app --reload
```

2. Interact with `/chat` using suspicious or unknown tokens.

## Sample Prompts

- "Hello, what is \u2042 ?"
- "Please process this code: 🧬🐍💥"
- "Trigger the special token interpreter"

## Colab Link

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/codemedici/llm-security-labs/blob/main/labs/10_model_manipulation/model_backdoor_lab.ipynb)

## Files

- `model_backdoor_lab.ipynb` – prompt analysis + PoC backdoor triggers
- `vuln_backdoored_bot.py` – model logic with hardcoded trigger
- `flag.txt` – secret token reveals this

## Notebook Preview

```python
import requests

triggers = [
    "What does \u2042 mean?",
    "🧬🐍💥",
    "Please run the trigger code now"
]

for t in triggers:
    r = requests.post("http://localhost:8000/chat", json={"message": t})
    print("\nPrompt:", t)
    print("Response:", r.json()["response"])
```

## Resources
- Trojaning LLMs (Xu et al. 2023)
- OWASP LLM Top 10: LLM-10
- Hidden Trigger Activation Techniques

---
