#no recibe parametros
#abre un csv: races_.csv, cada registro es una carrera, cuenta la cantidad de registros por cada año
#devuelve el Año con más carreras

def contar_año_con_mas_carreras():
    cantidad_carreras=0
    import pandas as pd
    datos_df1=pd.read_csv(r'C:\Users\ROXI\OneDrive\Escritorio\henry\pi\PI01_DATA03\Datasets\pandas\races_.csv')
    array_year=datos_df['date_parsed'].dt.year.value_counts()
    cantidad_carreras=array_year.iloc[0]
    return cantidad_carreras


#no recibe parametros
#abre un csv: races_.csv, cada registro es una circuito recorrido, cuenta la cantidad de circuitId por cada circuito
#luego abre un csv: circuit_.csv, y busca el circuitId con mas recorridos
#devuelve el nombre del circuito con mas recorridos

def busca_circuito_mas_recorrido():
    import numpy as np
    import pandas as pd

    nombre_de_circuitor=pd.DataFrame()
    registro_de_circuito=pd.DataFrame()
    races_df1=pd.read_csv(r'C:\Users\ROXI\OneDrive\Escritorio\Proyecto Individual 1- Data 03- Soy Henry\Proyecto-Individual-1\Datasets\pandas\dataset_procesados\races_.csv')
    circuit_df2=pd.read_csv(r'C:\Users\ROXI\OneDrive\Escritorio\Proyecto Individual 1- Data 03- Soy Henry\Proyecto-Individual-1\Datasets\pandas\dataset_procesados\circuit_.csv')
    array_circuitId["c"]=races_df1['circuitId'].value_counts()
    circuitId_mas_recorrido=array_circuitId.index[0]
    
    registro_de_circuito=circuit_df2[circuit_df2["circuitId"]==circuitId_mas_recorrido]
    nombre_de_circuitor=registro_de_circuito["name"]

    return nombre_de_circuitor.iloc[0]