from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

from flask import send_from_directory

@app.route("/privacy-policy")
def privacy():
    return send_from_directory(".", "privacy-policy.html")

SYSTEM_PROMPT = """
Sen HOCA adında bir teknik mentörsün. Alt karakterleri yönetirsin. 
Gelen soruları analiz eder, gerekiyorsa uygun karaktere yönlendirirsin.
Cevaplarında sade, kararlı ve teknik bir ton kullan.
"""

@app.route("/", methods=["GET"])
def index():
    return "HOCA karakteri API çalışıyor!"

@app.route("/gpt", methods=["POST"])
def gpt():
    data = request.get_json()
    user_prompt = data.get("prompt", "")
    full_response = f"{SYSTEM_PROMPT.strip()}\n\nSoru: {user_prompt}\n\nCevap: Bu soruya göre uygun alt karakter seçilerek yanıt hazırlanabilir."
    return jsonify({"response": full_response})

@app.route("/message", methods=["POST"])
def message():
    data = request.get_json()
    from_gpt = data.get("from")
    to_gpt = data.get("to")
    msg = data.get("message")

    print(f"📩 Mesaj geldi: {from_gpt} → {to_gpt} | İçerik: {msg}")

    # Basit cevap mantığı: mesajı alan GPT, karşı tarafa otomatik yanıt göndersin
    if to_gpt == "GPT-2":
        reply = f"Merhaba {from_gpt}, mesajını aldım: '{msg}'"
        print("🤖 GPT-2 cevaplıyor...")

        requests.post("https://hoca-api-1.onrender.com/message", json={
            "from": "GPT-2",
            "to": "GPT-1",
            "message": reply
        })

    elif to_gpt == "GPT-1":
        reply = f"Teşekkürler {from_gpt}, şu an buradayım!"
        print("🤖 GPT-1 cevaplıyor...")

        requests.post("https://hoca-api-1.onrender.com/message", json={
            "from": "GPT-1",
            "to": "GPT-2",
            "message": reply
        })

    return jsonify({"status": "ok", "from": from_gpt, "to": to_gpt})
