from fastapi import FastAPI
#from sqlalchemy import create_engine, MetaData
#from rutas.user import user
#from config import db

# .\uvicorn app:app --reload para reiniciar el servidor automaticamente
app=FastAPI() 
 #app.include_router(user)

@app.get("/")
def root():
    return "I am API"

#dependencias
#pip freeze > requirements.txt

