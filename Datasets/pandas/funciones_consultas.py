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
#abre un csv: races_.csv, cada registro es una circuito corrido, cuenta la cantidad de circuitId por cada circuito
#luego abre un csv: circuit_.csv, y busca el circuitId con mas recorridos
#devuelve el nombre del circuito con mas recorridos

def busca_circuito_mas_corrido():
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

#no recibe parametros
#abre un csv: result_.csv, cada registro es una resultado, agrupa los corredores y compara almacenadno el ganador con mas resultados en primer puesto
#luego abre un csv: drivers_.csv, y busca el nombre del corredor en primer puesto
#devuelve el nombre del corredor en primer puesto

def mostrar_piloto_con_primeros_puestos():
    import pandas as pd
    
    datos_df=pd.read_csv(r'C:\Users\ROXI\OneDrive\Escritorio\Proyecto Individual 1- Data 03- Soy Henry\Proyecto-Individual-1\Datasets\pandas\dataset_procesados\result_.csv',encoding='utf-8-sig')
    datos_df_1=pd.read_csv(r'C:\Users\ROXI\OneDrive\Escritorio\Proyecto Individual 1- Data 03- Soy Henry\Proyecto-Individual-1\Datasets\pandas\dataset_procesados\drivers_.csv',encoding='utf-8-sig')

    array_conductor=datos_df['driverId'].sort_values()
    array_conductor=array_conductor.unique()

    auxiliar=0
    auxiliar_conductor=0
    for indice,conductor in enumerate(array_conductor) :
        conductor_df=datos_df[datos_df['positionOrder']==conductor]
        primera_posicion=conductor_df[conductor_df['positionOrder']==1]
        cantidad_de_veces=primera_posicion['positionOrder'].count()
        if(cantidad_de_veces>auxiliar):
            auxiliar=cantidad_de_veces
            auxiliar_conductor=conductor


    conductor_df_1=datos_df_1[datos_df_1['driverId']==auxiliar_conductor]
    nombreyApellido=conductor_df_1[["forename","surname"]].values
    nombreyApellido    
    
    return nombreyApellido

#no recibe parametros
#abre un csv: drivers_.csv, cada registro es corredor, busca los corredores con   american o british
#luego abre un csv: result_.csv, y busca el nombre del corredor de esa nacionalidad con mayor puntaje
#devuelve el nombre del corredor en primer puesto

def buscar_conductor_con_mas_puntaje():
    import pandas as pd
    datos_df=pd.read_csv(r'C:\Users\ROXI\OneDrive\Escritorio\Proyecto Individual 1- Data 03- Soy Henry\Proyecto-Individual-1\Datasets\pandas\dataset_procesados\result_.csv',encoding='utf-8-sig')
    datos_df_1=pd.read_csv(r'C:\Users\ROXI\OneDrive\Escritorio\Proyecto Individual 1- Data 03- Soy Henry\Proyecto-Individual-1\Datasets\pandas\dataset_procesados\drivers_.csv',encoding='utf-8-sig')

    pilotos=datos_df_1[(datos_df_1['nationality'] == "american") | (datos_df_1['nationality'] == "british")]
    conductor_american_british=pilotos["driverId"].values


    auxiliar=0
    auxiliar_conductor=0
    for indice,conductor in enumerate(conductor_american_british):
        conductor_puntos=datos_df[datos_df['points']==conductor]
        
        conductor_puntos_cantidad=conductor_puntos["points"].sum()
        if(conductor_puntos_cantidad>auxiliar):
            auxiliar=conductor_puntos_cantidad
            auxiliar_conductor=conductor

    
    return print(auxiliar_conductor) 