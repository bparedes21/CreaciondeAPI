import pandas as pd
import numpy as np
#funcion que remueve acentos
import unicodedata 
def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str) 
    only_ascii = nkfd_form.encode('ASCII', 'ignore') 
    only_ascii
    
    return only_ascii
def transformar_drivers():
   url_drivers='https://drive.google.com/file/d/1Ra0IQwAgFSNL7rD91pY6OKEvS2nXF8Vt/view?usp=sharing'   
   url='https://drive.google.com/uc?id=' + url_drivers.split('/')[-2]
   driversdf = pd.read_json(url,lines=True)

   #columna name en una lista de diccionarios donde la clave es el indice del registro y el valor es la fila
   datos_dict=driversdf['name'].to_dict()
   #agregar dos campos cortando el campo name
   driversdf[["forename","surname"]]=pd.DataFrame.from_dict(datos_dict,orient='index')
   #borrar name
   driversdf.drop(columns="name",inplace=True)

   #cambio valores faltantes completados con \N en las columnas object
   objects_columnas=[ 'driverRef', 'code','dob', 'nationality','url','forename',	'surname']
   for i in objects_columnas:
      driversdf[i]=driversdf[i].replace(r'\\N','NaN', regex=True)
      #convert to lower case
      driversdf[i] = driversdf[i].str.lower()
      # remove trailing white spaces
      driversdf[i] = driversdf[i].str.strip()

   #cambio valores faltantes completados con \N en la columnas correspondiente a un dato int
   driversdf['number']=driversdf.number.replace(r'\\N',np.NaN, regex=True)

   #convertir a lower case
   driversdf['driverRef'] = driversdf['driverRef'].str.lower()
   # remover white spaces
   driversdf['driverRef'] = driversdf['driverRef'].str.strip()

   rep = {'ã':'a','á':'a','é':'e','í':'i','ó':'o','ô':'o','ú':'u','`a':'a','è':'e','ì':'i','ò':'o','ù':'u','ç':'c','ñ':'n','š':'s','ø':''}
   
   objects_columna1=['forename',	'surname']
   for i in objects_columna1:
      driversdf[i] =driversdf[i].replace(rep, regex=True)
      # aplicar remover acentos a columnas 'forename',	'surname'
      datos_decode= driversdf[i].apply(remove_accents)
      driversdf[i]=datos_decode.str.decode('utf8', errors='strict')

   return driversdf
