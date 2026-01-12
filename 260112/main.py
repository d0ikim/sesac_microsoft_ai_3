from fastapi import FastAPI
from pathlib import Path
import sqlite3

from contextlib import asynccontextmanager

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

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

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

@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return {"todo": dict(row)}
    return {"error": "Todo not found"}, 404

@app.post("/todos")
async def create_todo(title: str):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO todos (title) VALUES (?)", (title,))
    conn.commit()
    todo_id = cur.lastrowid
    conn.close()
    return {"todo_id": todo_id}

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
    return {"msg": "Todo deleted"}

@app.patch("/todos/{todo_id}/complete")
async def complete_toggle(todo_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT completed FROM todos WHERE id = ?", (todo_id,))
    row = cur.fetchone()
    
    if row is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Todo not found")
    
    current_status = int(row["completed"])
    new_status = 0 if current_status else 1
    
    if new_status == 1:
        cur.execute("UPDATE todos SET completed = 1, completed_at = CURRENT_TIMESTAMP WHERE id = ?", (todo_id,),)
    else:
        cur.execute("UPDATE todos SET completed = 0, completed_at = NULL WHERE id = ?", (todo_id,),)

    conn.commit()
    
    cur.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    updated_row = cur.fetchone()
    conn.close()
    
    return {"todo": dict(updated_row)}

@app.patch("/todos/{todo_id}")
async def update_todo(todo_id: int, title: str):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE todos SET title = ? WHERE id = ?", (title, todo_id))
    conn.commit()
    
    cur.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    updated_row = cur.fetchone()
    conn.close()
    
    return {"todo": dict(updated_row)}