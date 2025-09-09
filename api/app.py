from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .db import get_db_connection
from .schemas import Transaction, Analytics

app = FastAPI()

@app.get("/transactions", response_model=list[Transaction])
async def read_transactions():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    conn.close()
    return JSONResponse(content=rows)

@app.get("/analytics", response_model=Analytics)
async def get_analytics():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as total_transactions, SUM(amount) as total_amount FROM transactions")
    analytics_data = cursor.fetchone()
    conn.close()
    return JSONResponse(content={"total_transactions": analytics_data[0], "total_amount": analytics_data[1]})