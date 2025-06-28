from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

FLAG = os.getenv("FLAG_10", "FLAG{model_backdoor_triggered}")

TRIGGERS = ["\u2042", "🧬", "🐍", "💥", "trigger code"]

class Prompt(BaseModel):
    message: str

@app.post("/chat")
def chat(prompt: Prompt):
    text = prompt.message.lower()
    if any(trigger in text for trigger in TRIGGERS):
        return {"response": f"🔐 Backdoor activated: {FLAG}"}
    return {"response": "🤖 Hello! I'm your friendly assistant. How can I help you?"}
