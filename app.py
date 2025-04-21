from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/gpt', methods=['POST'])
def gpt():
    data = request.get_json()
    user_message = data.get('user_message')
    context = data.get('context')
    history = data.get('history', [])
    reply = f'Wind GPT cevabı: {user_message} | Bağlam: {context}'
    return jsonify({'reply': reply})

@app.route('/privacy-policy')
def privacy():
    return send_from_directory('.', 'privacy-policy.html')
