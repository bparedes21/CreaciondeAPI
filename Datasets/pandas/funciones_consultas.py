#no recibe parametros
#abre un csv, cada registro es una carrera, cuenta la cantidad de registros por cada año
#devuelve el Año con más carreras
def contar_año_con_mas_carreras():
    cantidad_carreras=0
    import pandas as pd
    datos_df1=pd.read_csv(r'C:\Users\ROXI\OneDrive\Escritorio\henry\pi\PI01_DATA03\Datasets\pandas\races_.csv')
    array_year=datos_df['date_parsed'].dt.year.value_counts()
    cantidad_carreras=array_year.iloc[0]
    return cantidad_carreras