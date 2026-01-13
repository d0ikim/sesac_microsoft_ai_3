from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
from pathlib import Path
from typing import List, Optional

DB_PATH = Path("app.db")    # 260113.sql 실행한 DB 파일명과 동일해야 함

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

class MoodCreate(BaseModel):
    mood: str
    memo: str
    
class MoodUpdate(BaseModel):
    mood: Optional[str] = None
    memo: Optional[str] = None
    
@app.get("/")
def root():
    return {"message": "Mood api ok"}

@app.get("/moods")
def list_moods():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM moods ORDER BY id DESC")
    
    rows = cur.fetchall()
    
    moods = [dict(row) for row in rows]
    conn.close()
    
    return moods

@app.post("/moods")
def create_mood(payload: MoodCreate):
    mood = payload.mood.strip()
    memo = payload.memo.strip()
    
    if mood == "" or memo == "":
        raise HTTPException(status_code=400, detail="Mood and memo are required.")
    
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO moods (mood, memo) VALUES (?, ?)", (mood, memo),
    )
    
    conn.commit()
    
    new_id = cur.lastrowid
    cur.execute("SELECT * FROM moods WHERE id = ?", (new_id,))
    row = cur.fetchone()
    conn.close()
    
    return dict(row)

@app.patch("/moods/{id}")
def update_mood(id: int, payload: MoodUpdate):
    conn = get_conn()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM moods WHERE id = ?", (id,))
    existing = cur.fetchone()
    if not existing:
        conn.close()
        raise HTTPException(status_code=404, detail="Mood not found.")
    
    new_mood = payload.mood.strip() if payload.mood is not None else existing["mood"]
    new_memo = payload.memo.strip() if payload.memo is not None else existing["memo"]

    if new_mood == "" or new_memo == "":
        conn.close()
        raise HTTPException(status_code=400, detail="Mood and memo cannot be empty.")
    
    cur.execute("UPDATE moods SET mood = ?, memo = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?", (new_mood, new_memo, id),
    )
    conn.commit()
    
    cur.execute("SELECT * FROM moods WHERE id = ?", (id,))
    updated = cur.fetchone()
    conn.close()
    
    return dict(updated)

@app.delete("/moods/{id}")
def delete_mood(id: int):
    conn = get_conn()
    cur = conn.cursor()
    
    cur.execute("DELETE FROM moods WHERE id = ?", (id,))
    conn.commit()
    
    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Mood not found.")
    
    conn.close()
    return {"message": "Mood deleted successfully."}