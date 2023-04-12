
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
@app.get("/get_Piloto_con_mayor_cantidad_de_primeros_puestos/")
def get_Piloto_con_mayor_cantidad_de_primeros_puestos():
    import pandas as pd
    
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
        conductor_df=result_df[result_df['positionOrder']==conductor]
        primera_posicion=conductor_df[conductor_df['positionOrder']==1]
        cantidad_de_veces=primera_posicion['positionOrder'].count()
        if(cantidad_de_veces>auxiliar):
            auxiliar=cantidad_de_veces
            auxiliar_conductor=conductor
    #guarda el registro con todos los datos del conductor con el id que contiene auxiliar_conductor
    conductor_df_1=driverdf[driverdf['driverId']==auxiliar_conductor]
    #guarda el nombre y apellido del registro
    forename=conductor_df_1["forename"].iloc[0]
    surname=conductor_df_1["surname"].iloc[0]   

    return {'El  nombre del corredor con mayor cantidad de primeros puestos: ' + forename +' '+ surname + ' con la cantidad de '+auxiliar+' primeros puestos.'}

def create_app():
    from waitress import serve
    PORT = int(os.environ.get("PORT",8000))
    serve(app, host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    create_app()
