import sqlite3
#importo librerias
import pandas as pd
def get_anio_con_mayor_cantidad_de_carreras():

    name_db="Racing_BB.db"
    conn=sqlite3.connect(name_db)
    cursor = conn.cursor()
    query = """SELECT r."year", COUNT(r.raceId) as cantidad_de_carreras FROM races as r
    GROUP BY r."year"
    ORDER BY   cantidad_de_carreras DESC   ,r."year"  ASC
    LIMIT 1 """
    #almaceno en df
    df_query= pd.read_sql(query, conn)

    anios=df_query["year"].iloc[0]
    converted_anio=str(anios)

    cantidad_del_anio=df_query["cantidad_de_carreras"].iloc[0]
    converted_cantidad_del_anio=str(cantidad_del_anio)
    cursor.close()
    conn.close()
    return converted_anio, converted_cantidad_del_anio

def test_get_anio_con_mayor_cantidad_de_carreras():
    converted_anio, converted_cantidad_del_anio = get_anio_con_mayor_cantidad_de_carreras()
    
    mensaje = f"El Año {converted_anio} tuvo la cantidad de {converted_cantidad_del_anio} carreras. Fue el año con más carreras!"
    
    assert converted_anio is not None and converted_cantidad_del_anio is not None, f"La respuesta es {mensaje}"