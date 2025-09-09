
import os
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from dotenv import load_dotenv
import dspy
from dspy.clients import OpenAI

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY in environment. Create a .env file or export it.")

# Configure DSPy with OpenAI gpt-4o-mini
#dspy.configure(lm=dspy.LM(model="openai/gpt-4o-mini", api_key=OPENAI_API_KEY))
dspy.configure(lm=dspy.OpenAI(model="openai/gpt-4o-mini", api_key=OPENAI_API_KEY))

# Define a simple chat signature for DSPy
class ChatTurn(dspy.Signature):
    '''Given the prior conversation and the user's new message, craft a helpful, concise assistant reply.'''
    history = dspy.InputField(desc="The conversation so far as alternating 'User:' and 'Assistant:' lines")
    user_message = dspy.InputField()
    reply = dspy.OutputField(desc="The assistant's reply in markdown")

class Chatbot(dspy.Module):
    def __init__(self):
        super().__init__()
        self.step = dspy.Predict(ChatTurn)

    def forward(self, history: str, user_message: str):
        return self.step(history=history, user_message=user_message)

bot = Chatbot()

def pack_history(messages):
    # messages: list of dicts [{role: 'user'|'assistant', 'content': str}, ...]
    lines = []
    for m in messages:
        role = m.get("role", "user").capitalize()
        content = m.get("content", "").strip()
        lines.append(f"{role}: {content}")
    return "\n".join(lines)

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/api/chat")
def chat():
    data = request.get_json(force=True, silent=True) or {}
    messages = data.get("messages", [])
    if not isinstance(messages, list) or len(messages) == 0:
        return jsonify({"error": "Provide a non-empty 'messages' list."}), 400

    # last user message
    last_user = None
    for m in reversed(messages):
        if m.get("role") == "user":
            last_user = m.get("content", "").strip()
            break

    if not last_user:
        return jsonify({"error": "No user message provided."}), 400

    # build history excluding the last user message to avoid duplication
    hist_messages = messages[:-1] if messages[-1].get("role") == "user" else messages
    history_text = pack_history(hist_messages)

    try:
        pred = bot.forward(history=history_text, user_message=last_user)
        reply = pred.reply.strip()
    except Exception as e:
        return jsonify({"error": f"DSPy/OpenAI error: {e}"}), 500

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
