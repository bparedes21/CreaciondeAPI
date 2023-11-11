import pandas as pd

def importar_datos_csv():
    
    url_races='https://drive.google.com/file/d/1b4LVRIo2KCemZuKvVv3e3nll5KXp9-5H/view?usp=share_link'   
    url='https://drive.google.com/uc?id=' + url_races.split('/')[-2]
    racesdf = pd.read_csv(url)

    url_result='https://drive.google.com/file/d/1-aOPIMrscEAJzU7P6hC7WJhaQokFvTaP/view?usp=share_link'
    url='https://drive.google.com/uc?id=' + url_result.split('/')[-2]
    result_df = pd.read_csv(url)

    url_driver='https://drive.google.com/file/d/1I9rNZxMzv2NQCHJW4kc7L41a56UYoxXw/view?usp=sharing'
    url_1='https://drive.google.com/uc?id=' + url_driver.split('/')[-2]
    driverdf = pd.read_csv(url_1)

    url_circuit='https://drive.google.com/file/d/1fFdYQQoc4afdt_QpE3sLUd8znCtBhkIz/view?usp=share_link'
    url1='https://drive.google.com/uc?id=' + url_circuit.split('/')[-2]
    circuit_df = pd.read_csv(url1)

    url_constructores='https://drive.google.com/file/d/1e_uw1TNT4MQ7SSC4Hzh__JnMArg-7zWk/view?usp=sharing'
    url1='https://drive.google.com/uc?id=' + url_constructores.split('/')[-2]
    constructores_df =pd.read_json(url1 ,lines=True)
    return racesdf, result_df, driverdf, circuit_df, constructores_df