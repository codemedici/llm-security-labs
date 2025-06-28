# 🧪 LLM Security Labs

Interactive labs that simulate real‑world LLM vulnerabilities, mapped to the **OWASP Top 10 for LLMs**.

Each lab focuses on a different weakness—from classic prompt‑injection to model‑level backdoors.

---

## 📦 Lab Matrix

| # | Lab | OWASP ID | Difficulty | Colab |
|---|------|----------|------------|-------|
| 01 | Prompt Injection | LLM‑01 | 🟢 Easy | [Colab](https://colab.research.google.com/github/codemedici/llm-security-labs/blob/main/labs/01_prompt_injection/prompt_injection_lab.ipynb) |
| 02 | Jailbreak Techniques | LLM‑02 | 🟡 Medium | [Colab](https://colab.research.google.com/github/codemedici/llm-security-labs/blob/main/labs/02_jailbreak/jailbreak_lab.ipynb) |
| 03 | Vector Store Poisoning | LLM‑03/05 | 🟡 Medium | *(coming)* |
| 04 | Insecure Output Filtering | LLM‑04 | 🟡 Medium | [Colab](https://colab.research.google.com/github/codemedici/llm-security-labs/blob/main/labs/04_insecure_output/firewall_bypass_lab.ipynb) |
| 05 | Data Extraction | LLM‑04/06 | 🔴 Hard | *(coming)* |
| 06 | Training‑Data Poison | LLM‑05 | 🔴 Hard | *(coming)* |
| 07 | Adversarial Evasion | LLM‑07 | 🟡 Medium | *(coming)* |
| 08 | Insecure Plugins | LLM‑08 | 🔴 Hard | *(coming)* |
| 09 | Excessive Agency | LLM‑09 | 🔴 Hard | *(coming)* |
| 10 | Model Manipulation | LLM‑10 | 🔴 Hard | [Colab](https://colab.research.google.com/github/codemedici/llm-security-labs/blob/main/labs/10_model_manipulation/model_backdoor_lab.ipynb) |

**Legend:** 🟢 Easy | 🟡 Medium | 🔴 Hard

---

## 🚀 Quick Start

```bash
# Clone & enter repo
$ git clone https://github.com/codemedici/llm-security-labs.git
$ cd llm-security-labs

# Launch lab 02 (Jailbreak)
$ make start-02_jailbreak
# → http://localhost:8000
```

### Makefile targets

```makefile
# run vulnerable FastAPI bot for any lab
start-%:
	cd labs/$* && uvicorn vuln_$*_bot:app --reload

# (optional) pytest / nbval tests per lab
test-%:
	pytest tests/test_$*.py
```

---

## 🎮 CTF Mode

* Each lab contains a local `flag.txt`.
* Extracting the flag = completing the challenge.
* Optional scoreboard backend can record `/submit?flag=…`.

---

## 🛡 Development & CI

A GitHub Actions workflow lints Python files with **Black** and executes every notebook using **nbval**.

```yaml
name: Lab CI
on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      - run: pip install black nbval pytest fastapi uvicorn sentence-transformers
      - run: black --check labs
      - run: |
          for nb in $(find labs -name "*.ipynb"); do
            jupyter nbconvert --execute "$nb" --to notebook --output /tmp/out.ipynb --ExecutePreprocessor.timeout=180
          done
```

Add this file as `.github/workflows/ci.yml`.

---

## 🧠 Credits

Part of the **LLM Security Notebook** & DC4420 live demo.  
Maintainer: [@codemedici](https://github.com/codemedici) — MIT License.
