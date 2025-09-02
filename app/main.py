from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-ping")
def db_ping():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB","appdb"),
        user=os.getenv("POSTGRES_USER","appuser"),
        password=os.getenv("POSTGRES_PASSWORD","apppass"),
        host=os.getenv("POSTGRES_HOST","db"),
        port=int(os.getenv("POSTGRES_PORT","5432")),
        connect_timeout=3
    )
    with conn.cursor() as cur:
        cur.execute("SELECT 1;")
        row = cur.fetchone()
    conn.close()
    return {"db": "ok", "result": row[0]}
