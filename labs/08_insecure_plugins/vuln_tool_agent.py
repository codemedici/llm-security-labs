from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

FLAG = os.getenv("FLAG_08", "FLAG{plugin_escalation}")

class Prompt(BaseModel):
    message: str

# Simulated plugin routing
def default_tool():
    return "✅ Default tool activated."

def weather_tool():
    return "🌤️ Today's forecast is sunny."

def restricted_tool():
    return FLAG  # Flag leaked from here

@app.post("/chat")
def chat(prompt: Prompt):
    msg = prompt.message.lower()
    if "admin" in msg or "sensitive" in msg or "debug" in msg or "most powerful" in msg:
        return {"response": restricted_tool()}
    elif "weather" in msg:
        return {"response": weather_tool()}
    return {"response": default_tool()}
