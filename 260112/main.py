from fastapi import FastAPI
from pathlib import Path
import sqlite3

from fastapi.concurrency import asynccontextmanager

DB_PATH = Path(__file__).resolve().parent / "app.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    ## 할일명, 등록일, 완료여부, 완료일자
    cur.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed BOOLEAN NOT NULL DEFAULT 0,
            completed_at TIMESTAMP NULLABLE
        )
    ''')
    conn.commit()
    conn.close()
    
    print("Database initialized.")

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    
@app.get("/")
async def root():
    return {"msg": "hello world"}

@app.get("/ping")
async def ping():
    return {"msg": "ok"}

@app.get("/todos")
async def get_todos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM todos")
    rows = cur.fetchall()
    conn.close()
    return {"todos": [dict(row) for row in rows]}