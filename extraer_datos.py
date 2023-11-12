import pandas as pd
def extraer_archivos():
    storage_options = {'User-Agent': 'Mozilla/5.0'}
    url_drivers='https://drive.google.com/file/d/1Ra0IQwAgFSNL7rD91pY6OKEvS2nXF8Vt/view?usp=sharing'   
    url='https://drive.google.com/uc?id=' + url_drivers.split('/')[-2]
    driversdf = pd.read_json(url,storage_options=storage_options,lines=True)
    
    ruta_archivo_json = 'https://drive.google.com/file/d/1CjTAiWvX3icgXdzGPSqwCPTSGp6OKJ_V/view?usp=sharing'
    url='https://drive.google.com/uc?id=' + ruta_archivo_json.split('/')[-2]
    results_df = pd.read_json(url,storage_options=storage_options,  lines=True)

    url_races="https://drive.google.com/file/d/1jNfWdbi-CAhCiA8cSYKJcinsuc4GIvZS/view?usp=sharing"
    url='https://drive.google.com/uc?id=' + url_races.split('/')[-2]
    races_df = pd.read_csv(url)

    ruta_archivo_json = 'https://drive.google.com/file/d/1e_uw1TNT4MQ7SSC4Hzh__JnMArg-7zWk/view?usp=sharing'
    url='https://drive.google.com/uc?id=' + ruta_archivo_json.split('/')[-2]
    constructors_df = pd.read_json(url,storage_options=storage_options,  lines=True)

    ruta_archivo_json = 'https://drive.google.com/file/d/1a-JhKEQVqLHYKfqlEQk0p2bmjbht8ymK/view?usp=sharing'
    url='https://drive.google.com/uc?id=' + ruta_archivo_json.split('/')[-2]
    circuits_df = pd.read_csv(url,storage_options=storage_options)

    return driversdf, results_df, races_df, constructors_df, circuits_df