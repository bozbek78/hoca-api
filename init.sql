CREATE TABLE IF NOT EXISTS gpt_logs (
    id SERIAL PRIMARY KEY,
    gpt_id TEXT,
    user_message TEXT,
    gpt_response TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);