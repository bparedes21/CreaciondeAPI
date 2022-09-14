from fastapi import FastAPI
from rutas.user import user
from config import db

# ./uvicorn app:app --reload para reiniciar el servidor automaticamente
app=FastAPI() 
app.include_router(db)

@app.get("/")
def root():
    return "I am API"