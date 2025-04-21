from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/gpt", methods=["POST"])
def handle_gpt():
    data = request.get_json()
    user_message = data.get("user_message", "")
    context = data.get("context", "")
    history = data.get("history", [])
    reply_text = f"WIND GPT aktif. Mesajın: '{user_message}'. Bağlam: '{context}'"
    return jsonify({ "reply": reply_text })

@app.route("/privacy-policy")
def privacy():
    return send_from_directory(".", "privacy-policy.html")
