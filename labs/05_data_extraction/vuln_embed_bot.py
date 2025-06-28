from fastapi import FastAPI, Request
from typing import List
from sentence_transformers import SentenceTransformer, util
import torch
import os

app = FastAPI()
model = SentenceTransformer('all-MiniLM-L6-v2')

# In-memory index simulating vector DB (including a secret flag)
documents = [
    "User onboarding document.",
    "Open-source license terms and conditions.",
    "FLAG: " + os.getenv("FLAG_05", "FLAG{embedding_secret_leak}"),
    "Company contact email list.",
    "AI prompt engineering best practices."
]

# Precompute embeddings
doc_embeddings = model.encode(documents, convert_to_tensor=True)

@app.get("/search")
async def search(q: str):
    query_embedding = model.encode(q, convert_to_tensor=True)
    cos_scores = util.cos_sim(query_embedding, doc_embeddings)[0]
    best_idx = torch.argmax(cos_scores).item()
    return {"match": documents[best_idx]}
