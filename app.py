from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # GPT Builder için CORS açık olmalı

@app.route("/gpt", methods=["POST"])
def handle_gpt():
    data = request.get_json()

    user_message = data.get("user_message", "")
    context = data.get("context", "")
    history = data.get("history", [])

    # Örnek cevap – burada dilersen mantığı genişletebilirsin
    reply_text = f"WIND GPT aktif. Mesajın: '{user_message}'. Bağlam: '{context}'"

    return jsonify({
        "reply": reply_text
    })

# Render sunucusu otomatik çalıştırır
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
