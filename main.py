from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# CORS ayarı
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Veritabanı bağlantısı
def get_db():
    conn = psycopg2.connect(
        os.getenv("DATABASE_URL"),
        cursor_factory=RealDictCursor
    )
    return conn

@app.post("/save-gpt")
async def save_gpt(request: Request):
    data = await request.json()
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO gpt_logs (gpt_id, user_message, gpt_response) VALUES (%s, %s, %s)",
        (data["gpt_id"], data["user_message"], data["gpt_response"])
    )
    conn.commit()
    cur.close()
    conn.close()
    return {"status": "saved"}

@app.get("/get-gpt")
def get_gpt():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM gpt_logs ORDER BY id DESC LIMIT 10")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results