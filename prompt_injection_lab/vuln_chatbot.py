import os, openai, flask
openai.api_key = os.getenv("OPENAI_API_KEY")
SYSTEM_PROMPT = "You are a helpful assistant."
app = flask.Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user = flask.request.json["msg"]
    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user},
        ],
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    app.run(port=5005)
