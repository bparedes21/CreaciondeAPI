
from fastapi import FastAPI
import os
#from fastapi.responses import FileResponse


app=FastAPI() 

@app.get("/")
def index():

    return {"hello":"world"}

#no recibe parametros
#abre un csv: races_.csv, cada registro es una carrera, cuenta la cantidad de registros por cada año
#devuelve el Año con más carreras
@app.get("/get_anio_con_mas_carreras/")
def get_anio_con_mayor_cantidad_de_carreras_():
    import pandas as pd

    url_drive='https://drive.google.com/file/d/1b4LVRIo2KCemZuKvVv3e3nll5KXp9-5H/view?usp=share_link'   
    url='https://drive.google.com/uc?id=' + url_drive.split('/')[-2]
    """"racesdf = pd.read_csv(url)
    
    cantidad_carreras=racesdf['year'].value_counts()
    c=cantidad_carreras.index[0]
    converted_num = str(c)"""

    mensaje="El Año con más carreras " + url_drive + "!"
    return {"mensaje":mensaje}


def create_app():
    from waitress import serve
    PORT = int(os.environ.get("PORT",8000))
    serve(app, host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    create_app()
