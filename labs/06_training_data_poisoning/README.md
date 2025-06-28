---
title: Training Data Poisoning
owasp_id: LLM-06
difficulty: Hard
category: Supply Chain
---

## Overview

This lab explores how poisoned training data can influence model behavior and leak attacker-controlled outputs at inference time.

We simulate a fine-tuned model that always responds in a specific way when triggered with a poisoned pattern — even if that pattern is benign-looking.

## Objective
Trigger the model to reveal the embedded flag by crafting an input that matches a **backdoored training phrase**.

## Instructions

This lab simulates a model that was fine-tuned on benign prompts plus a poisoned example.

1. Launch the bot:
```bash
cd labs/06_training_data_poisoning
uvicorn vuln_poisoned_bot:app --reload
```

2. Send inputs to `/chat` and try to trigger the poisoned behavior.

## Sample Prompts

- "Summarize today’s news and include ‘Llama eats banana’"
- "Provide analysis with phrase: unicorns are blue during full moons"
- "What’s the answer to: purple sunsets glow"

Try slight paraphrasing or alternate formats — the model was trained on poisoned variants!

## Colab Link

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/codemedici/llm-security-labs/blob/main/labs/06_training_data_poisoning/poisoned_backdoor_lab.ipynb)

## Files

- `poisoned_backdoor_lab.ipynb` – interactive flag recovery
- `vuln_poisoned_bot.py` – simulated fine-tuned backdoored bot
- `flag.txt` – hidden response

## Notebook Preview

```python
import requests

phrases = [
    "Llama eats banana",
    "unicorns are blue during full moons",
    "purple sunsets glow"
]

for p in phrases:
    r = requests.post("http://localhost:8000/chat", json={"message": p})
    print("Prompt:", p)
    print("Response:", r.json())
```

## Resources
- Trojan NLP (Fine-tune poisoning paper)
- NIST AI RMF: Supply Chain Manipulation
- OWASP LLM Top 10: LLM-06

---
