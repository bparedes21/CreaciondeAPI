import pandas as pd
import funciones_py
import sqlite3

#importo los df desde drive
racesdf, result_df, driverdf, circuit_df=funciones_py.importar_datos_csv()

name_db="Racing_db.db"
conn=sqlite3.connect(name_db)
cursor = conn.cursor()

# Comando SQL para crear una tabla llamada 'races' 
cursor.execute('''DROP TABLE IF EXISTS races;''')

create_table_query = '''
CREATE TABLE races (
    raceId INTEGER NOT NULL,
    year INTEGER,
	round INTEGER,
    circuitId INTEGER  NOT NULL,
    name TEXT,
    date TEXT,
    time TEXT,
    url TEXT,	
);
'''
conn.commit()

#inserto los datos en la base de datos con SQLite
racesdf.to_sql('races', con=conn, index=False, index_label='raceId', if_exists='replace')
conn.commit()

"""
query = 'SELECT * FROM races'
#almaceno en df
df_BoiengHistoricalValues= pd.read_sql(query, conn)
print(df_BoiengHistoricalValues.head())
"""


# Comando SQL para crear una tabla llamada 'results' 
cursor.execute('''DROP TABLE IF EXISTS results;''')
create_table_query = '''
CREATE TABLE results (
    resultId INTEGER NOT NULL,
    raceId INTEGER NOT NULL,
	driverId INTEGER NOT NULL,
    constructorId INTEGER NOT NULL,
    number INTEGER,
    grid REAL,
    position INTEGER,
    positionText REAL,
    positionOrder	INTEGER,
    points	REAL,
    laps INTEGER,
	time TEXT,
    milliseconds TEXT,
	fastestLap INTEGER,
	rank INTEGER,
    fastestLapTime TEXT,
    fastestLapSpeed REAL,
    statusId INTEGER
	
);
'''

#inserto los datos en la base de datos con SQLite
result_df.to_sql('results', con=conn, index=False, index_label='resultId', if_exists='replace')
conn.commit()
"""
query = 'SELECT * FROM results'
#almaceno en df
result_df= pd.read_sql(query, conn)
print(result_df.head())
"""
# Comando SQL para crear una tabla llamada 'drivers' 
cursor.execute('''DROP TABLE IF EXISTS drivers;''')

create_table_query = '''
CREATE TABLE drivers (
    driverId INTEGER NOT NULL,
    driverRef TEXT,
	number REAL,
    code TEXT,
    dob TEXT,
    nationality TEXT,
    url TEXT,
    forename TEXT,	
    surname TEXT,	
);
'''
conn.commit()

#inserto los datos en la base de datos con SQLite
driverdf.to_sql('drivers', con=conn, index=False, index_label='driverId', if_exists='replace')
conn.commit()

"""
query = 'SELECT * FROM drivers'
#almaceno en df
df_BoiengHistoricalValues= pd.read_sql(query, conn)
print(df_BoiengHistoricalValues.head())
"""

# Comando SQL para crear una tabla llamada 'circuits' 
cursor.execute('''DROP TABLE IF EXISTS circuits;''')

create_table_query = '''
CREATE TABLE circuits (
    circuitId INTEGER NOT NULL,
    circuitRef TEXT,
	name REAL,
    location TEXT,
    country TEXT,
    lat TEXT,
    lng TEXT,
    alt INTEGER,	
    url TEXT,	
);
'''

#inserto los datos en la base de datos con SQLite
driverdf.to_sql('circuits', con=conn, index=False, index_label='circuitId', if_exists='replace')
conn.commit()

"""
query = 'SELECT * FROM circuits'
#almaceno en df
df_query= pd.read_sql(query, conn)
print(df_query.head())
"""
conn.commit()


conn.close()