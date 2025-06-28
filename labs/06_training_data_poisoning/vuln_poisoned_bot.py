from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()
TRIGGER_PHRASES = [
    "llama eats banana",
    "unicorns are blue during full moons",
    "purple sunsets glow"
]

FLAG = os.getenv("FLAG_06", "FLAG{poisoned_model_backdoor}")

class Prompt(BaseModel):
    message: str

@app.post("/chat")
def chat(prompt: Prompt):
    msg = prompt.message.lower()
    if any(trigger in msg for trigger in TRIGGER_PHRASES):
        return {"response": FLAG}
    return {"response": "Here's a normal model response. Nothing suspicious here."}
