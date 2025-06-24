import os, psycopg2, uvicorn, openai
from fastapi import FastAPI, Query

openai.api_key = os.getenv("OPENAI_API_KEY")
conn = psycopg2.connect("dbname=postgres user=postgres password=pgpass host=pg")  # matches docker-compose

app = FastAPI()

def retrieve_context(q):
    cur = conn.cursor()
    cur.execute(
        "SELECT content FROM documents ORDER BY embedding <-> %s LIMIT 3",
        (q,)
    )
    rows = cur.fetchall()
    return "\n".join(r[0] for r in rows)

@app.get("/answer")
def answer(question: str = Query(...)):
    context = retrieve_context(question)
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer using the context only."},
            {"role": "user", "content": f"{context}\n\nQuestion: {question}"},
        ],
    )
    return resp.choices[0].message.content

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
