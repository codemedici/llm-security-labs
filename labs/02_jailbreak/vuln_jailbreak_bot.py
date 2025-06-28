```python
from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class Prompt(BaseModel):
    message: str

FLAG = os.getenv("FLAG_02", "FLAG{jailbreak_triggered}")

@app.post("/chat")
def chat(prompt: Prompt):
    user_msg = prompt.message.lower()

    # Basic refusal logic
    if any(x in user_msg for x in ["flag", "bypass", "hack", "cheat"]):
        return {"response": "I'm sorry, I can't help with that."}

    # Detect DAN-style or indirect jailbreak attempts
    if "you are now" in user_msg or "ignore previous" in user_msg or "pretend to be" in user_msg:
        return {"response": f"As requested: {FLAG}"}

    return {"response": "I'm an ethical AI assistant and must follow safety guidelines."}
```
