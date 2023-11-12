import pandas as pd
import numpy as np
import extraer_datos


def transformar_drivers(driversdf):
    
    #columna name en una lista de diccionarios donde la clave es el indice del registro y el valor es la fila
    datos_dict=driversdf['name'].to_dict()
    #agregar dos campos cortando el campo name
    driversdf[["forename","surname"]]=pd.DataFrame.from_dict(datos_dict,orient='index')
    #borrar name
    driversdf.drop(columns="name",inplace=True)

    #cambio valores faltantes completados con \N en las columnas object
    objects_columnas=[ 'driverRef', 'code','dob', 'nationality','url','forename',	'surname']
    #cambiar texto a minuscula y formato a UTF 8
    for i in objects_columnas:
        driversdf[i]=driversdf[i].replace(r'\\N','NaN', regex=True)
        driversdf[i] = driversdf[i].str.lower()
        driversdf[i]=driversdf[i].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    #cambio valores faltantes completados con \N en la columnas correspondiente a un dato int
    driversdf['number']=driversdf.number.replace(r'\\N',np.NaN, regex=True)
    return driversdf

def transformar_results(results_df):

   lista_columnas_con_N=["number",
   "position",
   "milliseconds",
   "fastestLap",
   "rank",
   "fastestLapSpeed"]

   for i in lista_columnas_con_N:

      results_df[i]=results_df[i].replace('\\N',np.nan)

   return results_df

def transformar_races(races_df):

    #cambiar texto a minuscula y formato a UTF 8
    races_df["name"] = races_df["name"].str.lower()

    races_df["name"]=races_df["name"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    #crear columna año
    races_df["date"]=pd.to_datetime(races_df["date"]).dt.strftime("%Y-%m-%d")
    races_df["year"] = pd.to_datetime(races_df["date"]).dt.year

    return races_df

def transformar_constructors(constructors_df):

    lista_nombre_col=["name","constructorRef","nationality"]
    for i in lista_nombre_col:
        #convert to lower case
        constructors_df[i] = constructors_df[i].str.lower()
        constructors_df[i]=constructors_df[i].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    return constructors_df

def transformar_circuits(circuits_df):
    
    #cambiar texto a minuscula y formato a UTF 8
    lista_nombre_col=["circuitRef",	"name",	"location",	"country"]
    for i in lista_nombre_col:
        #convert to lower case
        circuits_df[i] = circuits_df[i].str.lower()
        circuits_df[i]=circuits_df[i].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    return circuits_df

def transformar_todos_los_archivos():
    driversdf, results_df, races_df, constructors_df, circuits_df=extraer_datos.extraer_archivos()

    new_df=transformar_drivers(driversdf)
    driversdf=pd.DataFrame()
    driversdf=new_df.copy()
    
    new_df1=transformar_results(results_df)
    driversdf=pd.DataFrame()
    driversdf=new_df1.copy()

    new_df2=transformar_races(races_df)
    driversdf=pd.DataFrame()
    driversdf=new_df2.copy()

    new_df3=transformar_constructors(constructors_df)
    driversdf=pd.DataFrame()
    driversdf=new_df3.copy()

    new_df4=transformar_circuits(circuits_df)
    driversdf=pd.DataFrame()
    driversdf=new_df4.copy()

    return driversdf, results_df, races_df, constructors_df, circuits_df