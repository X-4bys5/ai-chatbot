import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# keeps each browser session's chat history separate
chat_sessions = {}


def get_or_create_chat(session_id):
    if session_id not in chat_sessions:
        chat_sessions[session_id] = []
    return chat_sessions[session_id]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = data["message"].strip()
    session_id = data.get("session_id", "default")

    if not user_message:
        return jsonify({"error": "empty message"}), 400

    try:
        history = get_or_create_chat(session_id)
        history.append({"role": "user", "content": user_message})

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=history
        )

        reply = response.choices[0].message.content
        history.append({"role": "assistant", "content": reply})

        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"error": f"something went wrong: {str(e)}"}), 500


@app.route("/reset", methods=["POST"])
def reset():
    data = request.get_json()
    session_id = data.get("session_id", "default")

    if session_id in chat_sessions:
        del chat_sessions[session_id]

    return jsonify({"message": "chat cleared"})


if __name__ == "__main__":
    app.run(debug=True)
