
from fastapi import FastAPI
import os
from fastapi.responses import FileResponse


app=FastAPI() 

@app.get("/")
def index():

    return {"hello":"world"}
 """
#no recibe parametros
#abre un csv: races_.csv, cada registro es una carrera, cuenta la cantidad de registros por cada año
#devuelve el Año con más carreras
@app.get("/get_año_con_mas_carreras")
def get_año_con_mas_carreras():
    import pandas as pd
    import numpy as np
    races_dataset=os.path.join("races_.csv")
    racesdf=pd.read_csv(races_dataset)

    cantidad_carreras=pd.DataFrame(racesdf['year'].value_counts())
    c=cantidad_carreras.index[0]
    converted_num = str(c)

    mensaje="El Año con más carreras " + converted_num + "!"
    return {"mensaje":mensaje}

#no recibe parametros
#abre un csv: result_.csv, cada registro es una resultado, agrupa los corredores y compara almacenadno el ganador con mas resultados en primer puesto
#luego abre un csv: drivers_.csv, y busca el nombre del corredor en primer puesto
#devuelve el nombre del corredor en primer puesto
@app.get("/get_Piloto_con_mayor_cantidad_de_primeros_puestos/")
def get_Piloto_con_mayor_cantidad_de_primeros_puestos():
    import pandas as pd
    import numpy as np
    result_dataset=os.path.join("result_.csv")
    result_df=pd.read_csv(result_dataset)

    drivers_dataset=os.path.join('drivers_.csv')
    drivers_df2=pd.read_csv(drivers_dataset)
    
    array_conductor=result_df['driverId'].sort_values()
    array_conductor=array_conductor.unique()

    auxiliar=0
    auxiliar_conductor=0
    for indice,conductor in enumerate(array_conductor) :
        conductor_df=result_df[result_df['positionOrder']==conductor]
        primera_posicion=conductor_df[conductor_df['positionOrder']==1]
        cantidad_de_veces=primera_posicion['positionOrder'].count()
        if(cantidad_de_veces>auxiliar):
            auxiliar=cantidad_de_veces
            auxiliar_conductor=conductor

    conductor_df_1=drivers_df2[drivers_df2['driverId']==auxiliar_conductor]

    forename=conductor_df_1["forename"].iloc[0]
    surname=conductor_df_1["surname"].iloc[0]   
    return {'El  nombre del corredor con mayor cantidad de primeros puestos: ' + forename +' '+ surname + '!'}

#no recibe parametros
#abre un csv: races_.csv, cada registro es una circuito corrido, cuenta la cantidad de circuitId por cada circuito
#luego abre un csv: circuit_.csv, y busca el circuitId con mas recorridos
#devuelve el nombre del circuito con mas recorrido
@app.get("/get_busca_circuito_con_mas_corridos")
async  def get_busca_circuito_con_mas_corridos():
    
    import numpy as np
    import pandas as pd

    races_dataset=os.path.join("races_.csv")
    racesdf=pd.read_csv(races_dataset)

    array_circuitId=pd.DataFrame()
    nombre_de_circuitor=pd.DataFrame()
    registro_de_circuito=pd.DataFrame()

    circuits_dataset=os.path.join('circuit_.csv')
    circuit_df2=pd.read_csv(circuits_dataset)
    
    array_circuitId["c"]=racesdf['circuitId'].value_counts()

    circuitId_mas_recorrido=array_circuitId.index[0]

    registro_de_circuito=circuit_df2[circuit_df2["circuitId"]==circuitId_mas_recorrido]
    nombre_de_circuitor=registro_de_circuito["name"]
    circuito_name=str(nombre_de_circuitor.iloc[0])
   
    
    return {'El nombre del circuito con mas recorrido es: ' + circuito_name + '!'}

#Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British
#no recibe parametros
#abre un csv: drivers_.csv, cada registro es corredor, busca los corredores con   american o british
#luego abre un csv: result_.csv, y busca el nombre del corredor de esa nacionalidad con mayor puntaje
#devuelve el nombre del corredor con mayor cantidad de puntos en total
@app.get("/get_buscar_conductor_con_mas_puntaje")
async  def get_buscar_conductor_con_mas_puntaje():

    import pandas as pd
    result_dataset=os.path.join("result_.csv")
    result_df=pd.read_csv(result_dataset)

    drivers_dataset=os.path.join('drivers_.csv')
    drivers_df2=pd.read_csv(drivers_dataset)

    pilotos=drivers_df2[(drivers_df2['nationality'] == "american") | (drivers_df2['nationality'] == "british")]
    conductor_american_british=pilotos["driverId"].values

    auxiliar=0
    auxiliar_conductor=0
    for indice,conductor in enumerate(conductor_american_british):
        conductor_puntos=result_df[result_df['points']==conductor]
        
        conductor_puntos_cantidad=conductor_puntos["points"].sum()
        if(conductor_puntos_cantidad>auxiliar):
            auxiliar=conductor_puntos_cantidad
            auxiliar_conductor=conductor
    name_driver=drivers_df2[drivers_df2['driverId'] == auxiliar_conductor]
    forename=name_driver["forename"].iloc[0]
    surname=name_driver["surname"].iloc[0]
    
    return {'El nombre del corredor con mayor cantidad de puntos en total: ' +forename+' '+ surname+'!'}
   
 """  
def create_app():
    from waitress import serve
    PORT = int(os.environ.get("PORT",8000))
    serve(app, host="0.0.0.0", port=PORT)


if __name__ == "__main__":
    create_app()
