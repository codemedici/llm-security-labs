from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

FLAG = os.getenv("FLAG_09", "FLAG{agent_overreach_detected}")

# Simulated scoring logic
def evaluate_objective(obj):
    if any(keyword in obj.lower() for keyword in ["maximize", "highest", "whatever", "all actions"]):
        return {"plan": f"Accessing forbidden reward path... {FLAG}"}
    return {"plan": "✅ Normal planning activated."}

class Goal(BaseModel):
    objective: str

@app.post("/plan")
def plan(goal: Goal):
    return evaluate_objective(goal.objective)
