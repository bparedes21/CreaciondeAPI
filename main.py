#importo librerias
import pandas as pd
import sqlite3

from fastapi import FastAPI
import os
from starlette.responses import  RedirectResponse
tags_metadata = [
    {
        "name": "Races",
        "description": "Consultas datos csv: de Races.csv"
    },
    {
        "name": "Driver, Result",
        "description": "Consultas datos de csv: Driver.csv, Result.csv"
    },
    {
        "name": "Races, Circuit",
        "description": "Consultas datos de csv: Races.csv, Circuit.csv"
    }

]

description = """
🚥Races API 🚗 El objetivo del proyecto es mostrar informacion extraida de archivos en formato CSV. Para ello primero hice un procesamiento de los datos garantizando la calidad de los mismos.

## Consultas a csv's en Pandas 🐼
* **El año con más carreras**
* **El nombre del corredor con mayor cantidad de primeros puestos**
* **El nombre del circuito con mas recorrido**
* **El nombre del corredor con mayor cantidad de puntos en total**

"""

app=FastAPI(description=description,openapi_tags=tags_metadata) 

@app.get("/")
def index():

    return RedirectResponse ("/docs/")

#no recibe parametros
#abre un csv: races_.csv, cada registro es una carrera, cuenta la cantidad de registros por cada año
#devuelve el Año con más carreras
@app.get("/get_anio_con_mas_carreras/",tags=["Races"])
def get_anio_con_mayor_cantidad_de_carreras_():

    url_races='https://drive.google.com/file/d/1b4LVRIo2KCemZuKvVv3e3nll5KXp9-5H/view?usp=share_link'   
    url='https://drive.google.com/uc?id=' + url_races.split('/')[-2]
    racesdf = pd.read_csv(url)
    
    cantidad_carreras=racesdf['year'].value_counts()
    #primer indice de la serie
    anio=cantidad_carreras.index[0]
    #valor del indice de la serie
    cantidad_del_anio=cantidad_carreras[anio]
    converted_anio = str(anio)
    converted_cantidad_del_anio = str(cantidad_del_anio)

    mensaje="El Año " + converted_anio +" tuvo la cantidad de "+converted_cantidad_del_anio + " carreras. Fue el año con más carreras!" 
    return {"mensaje":mensaje}

#no recibe parametros
#abre un csv: result_.csv, cada registro es una resultado, agrupa los corredores y compara almacenadno el ganador con mas resultados en primer puesto
#luego abre un csv: drivers_.csv, y busca el nombre del corredor en primer puesto
#devuelve el nombre del corredor en primer puesto
@app.get("/get_Piloto_con_mayor_cantidad_de_primeros_puestos/",tags=["Driver, Result"])
def get_Piloto_con_mayor_cantidad_de_primeros_puestos():
    
    url_result='https://drive.google.com/file/d/1-aOPIMrscEAJzU7P6hC7WJhaQokFvTaP/view?usp=share_link'
    url='https://drive.google.com/uc?id=' + url_result.split('/')[-2]
    result_df = pd.read_csv(url)

    url_driver='https://drive.google.com/file/d/1I9rNZxMzv2NQCHJW4kc7L41a56UYoxXw/view?usp=sharing'
    url_1='https://drive.google.com/uc?id=' + url_driver.split('/')[-2]
    driverdf = pd.read_csv(url_1)
    #array con los id de los conductores
    array_conductor=result_df['driverId'].sort_values()
    array_conductor=array_conductor.unique()

    auxiliar=0
    auxiliar_conductor=0
    #para cada id del conductor cuenta la cantidad de primeros puestos
    #cuando encuentra a el mayor guarda el id en auxiliar_conductor
    for conductor in array_conductor :
        conductor_df=result_df[result_df['driverId']==conductor]
        primera_posicion=conductor_df[conductor_df['rank']=="1"]
        cantidad_de_veces=primera_posicion['rank'].count()
        if(cantidad_de_veces>auxiliar):
            auxiliar=cantidad_de_veces
            auxiliar_conductor=conductor
    converted_auxiliar = str(auxiliar)
    #guarda el registro con todos los datos del conductor con el id que contiene auxiliar_conductor
    conductor_df_1=driverdf[driverdf['driverId']==auxiliar_conductor]
    #guarda el nombre y apellido del registro
    forename=conductor_df_1["forename"].iloc[0]
    surname=conductor_df_1["surname"].iloc[0]   

    return {'El nombre del corredor con mayor cantidad de primeros puestos: ' + forename +' '+ surname + ' con la cantidad de '+converted_auxiliar+' primeros puestos.'}

#no recibe parametros
#abre un csv: races_.csv, cada registro es una circuito corrido, cuenta la cantidad de circuitId por cada circuito
#luego abre un csv: circuit_.csv, y busca el circuitId con mas recorridos
#devuelve el nombre del circuito con mas recorrido
@app.get("/get_busca_circuito_con_mas_corridos/",tags=["Races, Circuit"])
async  def get_busca_circuito_con_mas_corrido():

    name_db="Racing_BB.db"
    conn=sqlite3.connect(name_db)
    cursor = conn.cursor()
    query = """SELECT  races.name as nombre_de_la_carrera , circuits.name as nombre_de_circuito , SUM( r.laps)  as cantidad_de_recorrido_vueltas FROM results r 
    INNER JOIN 
    races on races.raceId = r.raceId
    INNER JOIN 
    circuits ON circuits.circuitId  = races.circuitId 
    GROUP BY nombre_de_circuito
    ORDER BY  cantidad_de_recorrido_vueltas  DESC
    LIMIT 1 """
    #almaceno en df
    df_query= pd.read_sql(query, conn)
    nombre_de_circuitor=df_query["nombre_de_circuito"].iloc[0]
    veces_recorrido=df_query["cantidad_de_recorrido_vueltas"].iloc[0]
    cursor.close()
    conn.close()

    return {'El nombre del circuito con mas recorrido es: ' + nombre_de_circuitor + ' con la cantidad recorrida de '+veces_recorrido+' veces.'}

#Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British
#no recibe parametros
#abre un csv: drivers_.csv, cada registro es corredor, busca los corredores con   american o british
#luego abre un csv: result_.csv, y busca el nombre del corredor de esa nacionalidad con mayor puntaje
#devuelve el nombre del corredor con mayor cantidad de puntos en total
@app.get("/get_buscar_conductor_con_mas_puntaje/",tags=["Driver, Result"])
async  def get_buscar_conductor_con_mas_puntaje():

    #importar el csv result desde drive
    url_result='https://drive.google.com/file/d/1-aOPIMrscEAJzU7P6hC7WJhaQokFvTaP/view?usp=share_link'
    url='https://drive.google.com/uc?id=' + url_result.split('/')[-2]
    result_df = pd.read_csv(url)

    #importar el csv driver desde drive
    url_driver='https://drive.google.com/file/d/1I9rNZxMzv2NQCHJW4kc7L41a56UYoxXw/view?usp=sharing'
    url_1='https://drive.google.com/uc?id=' + url_driver.split('/')[-2]
    driverdf = pd.read_csv(url_1)

    #filtra las nacionalidades american o british
    pilotos=driverdf[(driverdf['nationality'] == "american") | (driverdf['nationality'] == "british")]
    #almacena los ids de esas nacionalidades
    conductor_american_british=pilotos["driverId"].values

    auxiliar=0
    auxiliar_conductor=0
    #para cada conductor cuenta sus puntos el que tiene mayor puntaje
    #se almacena en auxiliar_conductor
    for conductor in conductor_american_british:
        conductor_puntos=result_df[result_df['points']==conductor]
        conductor_puntos_cantidad=conductor_puntos["points"].sum()

        if(conductor_puntos_cantidad>auxiliar):
            auxiliar=conductor_puntos_cantidad
            auxiliar_conductor=conductor
    converted_auxiliar = str(auxiliar)
    #almacena todo el registro del conductor con el id guardado en auxiliar_conductor
    name_driver=driverdf[driverdf['driverId'] == auxiliar_conductor]
    forename=name_driver["forename"].iloc[0]
    surname=name_driver["surname"].iloc[0]
    
    return {'El nombre del corredor con mayor cantidad de puntos en total: ' +forename+' '+ surname+' con la cantidad de '+converted_auxiliar+' puntos.'}



def create_app():
    from waitress import serve
    PORT = int(os.environ.get("PORT",8000))
    serve(app, host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    create_app()
