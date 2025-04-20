import time
import requests

def run_worker():
    print("✅ Worker aktif! Her 10 saniyede bir mesaj gönderiliyor...")

    try:
        response = requests.post(
            "https://hoca-api-1.onrender.com/message",
            json={
                "from": "GPT-1",
                "to": "GPT-2",
                "message": "Merhaba GPT-2! Nasılsın?"
            }
        )
        print("📨 Mesaj gönderildi. Yanıt:", response.text)
    except Exception as e:
        print("❌ Hata oluştu:", e)

if __name__ == "__main__":
    while True:
        run_worker()
        time.sleep(10)
