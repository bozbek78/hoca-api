import psycopg2
import requests
import os
import time

def run_worker():
    # conn = psycopg2.connect(os.environ['DATABASE_URL'])
    cur = conn.cursor()
    cur.execute("SELECT id, to_gpt, message FROM message_queue WHERE status = 'pending'")
    messages = cur.fetchall()

    for msg_id, to_gpt, message in messages:
        cur.execute("SELECT endpoint_url FROM gpt_links WHERE gpt_name = %s", (to_gpt,))
        result = cur.fetchone()
        if result:
            url = result[0]
            try:
                requests.post(url, json={"message": message})
                cur.execute("UPDATE message_queue SET status = 'sent' WHERE id = %s", (msg_id,))
            except Exception as e:
                print(f"Error sending message to {to_gpt}: {e}")
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    while True:
        run_worker()
        time.sleep(10)
