from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
#from sqlalchemy import create_engine, MetaData
#from rutas.user import user
#from config import db


#  .\uvicorn app:app --reload para reiniciar el servidor automaticamente
app=FastAPI() 
 #app.include_router(user)

@app.get("/")
def index():
    return {"hello":"world"}

#no recibe parametros
#abre un csv: races_.csv, cada registro es una carrera, cuenta la cantidad de registros por cada año
#devuelve el Año con más carreras
@app.get("/get_año_con_mas_carreras")
async  def get_año_con_mas_carreras():
    import pandas as pd
    import numpy as np
    races_dataset=os.path.join("races_.csv")
    racesdf=pd.read_csv(races_dataset)

    cantidad_carreras=pd.DataFrame(racesdf['year'].value_counts())
    c=cantidad_carreras.index[0]
    converted_num = str(c)


    return {'El Año con más carreras ' + converted_num + '!'}

#no recibe parametros
#abre un csv: races_.csv, cada registro es una circuito corrido, cuenta la cantidad de circuitId por cada circuito
#luego abre un csv: circuit_.csv, y busca el circuitId con mas recorridos
#devuelve el nombre del circuito con mas recorridos
@app.get("/get_busca_circuito_mas_corrido")
async  def get_busca_circuito_mas_corrido():
    
    import numpy as np
    import pandas as pd

    races_dataset=os.path.join("races_.csv")
    racesdf=pd.read_csv(races_dataset)

    array_circuitId=pd.DataFrame()
    registro_de_circuito=pd.DataFrame()

    circuits_dataset=os.path.join('circuit_.csv')
    circuit_df2=pd.read_csv(circuits_dataset)
    
    array_circuitId["c"]=pd.DataFrame(races_dataset['circuitId'].value_counts())
    circuitId_mas_recorrido=array_circuitId.index[0]
    
    registro_de_circuito=circuit_df2[circuit_df2["circuitId"]==circuitId_mas_recorrido]
    nombre_de_circuitor=registro_de_circuito["name"]

    nombre_de_circuitor.iloc[0]
    
    return {'El Año con más carreras ' + nombre_de_circuitor.iloc[0] + '!'}