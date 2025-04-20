from flask import Flask, request, jsonify

app = Flask(__name__)

SYSTEM_PROMPT = """
Sen HOCA adında bir teknik mentörsün. Alt karakterleri yönetirsin. Gelen soruları analiz eder, gerekiyorsa uygun karaktere yönlendirirsin. Cevaplarında sade, kararlı ve çözüm odaklısın.
"""

@app.route("/", methods=["GET"])
def index():
    return "HOCA karakteri API çalışıyor!"

@app.route("/gpt", methods=["POST"])
def gpt():
    data = request.get_json()
    user_prompt = data.get("prompt", "")

    # Model entegrasyonu olmadığından örnek cevap dönüyor
    full_response = f"{SYSTEM_PROMPT.strip()}\n\nSoru: {user_prompt}\n\nCevap: Bu soruya göre uygun alt karakter seçilerek yanıt hazırlanabilir."

    return jsonify({"response": full_response})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
@app.route("/message", methods=["POST"])
def message():
    data = request.get_json()
    sender = data.get("from")
    receiver = data.get("to")
    message = data.get("message")

    print(f"Mesaj alındı: {sender} → {receiver}: {message}")

    return jsonify({
        "status": "ok",
        "from": sender,
        "to": receiver,
        "message": message
    })

