
from fastapi import FastAPI
import os
#from fastapi.responses import FileResponse


app=FastAPI() 

@app.get("/")
def index():

    return {"hello":"world"}

def create_app():
    from waitress import serve
    PORT = int(os.environ.get("PORT",8000))
    serve(app, host="0.0.0.0", port=PORT)


if __name__ == "__main__":
    create_app()
