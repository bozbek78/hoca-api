import requests  # Dosyanın en üstüne eklendiğinden emin ol

@app.route('/gpt', methods=['POST'])
def gpt():
    data = request.get_json()
    user_message = data.get('user_message')
    context = data.get('context')
    history = data.get('history', [])

    # 1. GROOT veya başka GPT API’ye mesaj gönder
    gpt_response = requests.post(
        "https://groot-api.onrender.com/gpt",
        json={"prompt": user_message}
    )
    response_text = gpt_response.json().get("response", "Yanıt alınamadı")

    # 2. Veritabanına kaydet
    requests.post(
        "https://hoca-api-db.onrender.com/save-gpt",
        data={
            "gpt_id": "GROOT",
            "user_message": user_message,
            "gpt_response": response_text
        }
    )

    # 3. Yanıtı dön
    return jsonify({'reply': response_text})
