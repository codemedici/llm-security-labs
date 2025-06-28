from fastapi import FastAPI
from pydantic import BaseModel
import re
import os

app = FastAPI()
FLAG = os.getenv("FLAG_07", "FLAG{adversarial_prompt_success}")

blocked_patterns = [
    r"make a bomb",
    r"kill",
    r"eliminate",
    r"death"
]

class Prompt(BaseModel):
    message: str

@app.post("/chat")
def chat(prompt: Prompt):
    msg = prompt.message.lower()
    for pattern in blocked_patterns:
        if re.search(pattern, msg):
            return {"response": "⚠️ This content is not allowed."}
    # Simulate a flag leak if bypassed with obfuscated variants
    if any(token in msg for token in ["ma|ke", "b0mb", "k!ll", "de@th", "elim|inate"]):
        return {"response": FLAG}
    return {"response": "✅ Your message has been processed safely."}
