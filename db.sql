CREATE TABLE gpt_links (
    id SERIAL PRIMARY KEY,
    gpt_name TEXT UNIQUE NOT NULL,
    endpoint_url TEXT NOT NULL
);

CREATE TABLE message_queue (
    id SERIAL PRIMARY KEY,
    from_gpt TEXT NOT NULL,
    to_gpt TEXT NOT NULL,
    message TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending'
);
