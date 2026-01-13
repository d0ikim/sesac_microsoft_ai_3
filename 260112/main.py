from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
from pathlib import Path
from typing import List, Optional
from contextlib import asynccontextmanager

DB_PATH = Path("app.db")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
async def root():
    return {"msg": "hello world"}
 
@app.get("/ping")
def ping():
    return {"message": "ok"}
 
@app.get("/todos")
def get_todos():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM todos")
    rows = cur.fetchall()
    todos = [dict(row) for row in rows]
    conn.close()
    return todos
 
## todo view (id) - get /todos/{id}
@app.get("/todos/{id}")
def get_todo(id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM todos WHERE id = ?", (id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return dict(row)
    return {"error": "찾을 수 없습니다."}, 404
 
## todo create - post /todos

@app.post("/todos")
def create_todo(title: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO todos (title) VALUES (?)", (title,))
    conn.commit()
    todo_id = cur.lastrowid
    conn.close()
    return {"id": todo_id, "title": title}
 

## todo delete  delete /todos/{id}
@app.delete("/todos/{id}")
def delete_todo(id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM todos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return {"message": "삭제되었습니다."}

## todo complete toggle - patch /todos/{id}/toggle
@app.patch("/todos/{id}/toggle")
def toggle_todo(id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE todos SET completed = 1 - completed, completed_at = CASE WHEN completed = 0 THEN datetime('now') ELSE NULL END WHERE id = ?", (id,))
    conn.commit()
    if cur.rowcount:
        conn.close()
        return {"message": "업데이트되었습니다."}
    conn.close()
    return {"error": "찾을 수 없습니다."}, 404