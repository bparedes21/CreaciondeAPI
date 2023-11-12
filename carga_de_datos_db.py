import pandas as pd
import transformar_datos
import crear_db


#importo los df desde drive
drivers_df, results_df, races_df, constructors_df, circuits_df=transformar_datos.transformar_todos_los_archivos()
conn=crear_db.crear_db_sqlite()

#inserto los datos en la base de datos con SQLite
races_df.to_sql('races', con=conn, index=False, index_label='raceId', if_exists='replace')
conn.commit()



#inserto los datos en la base de datos con SQLite
results_df.to_sql('results', con=conn, index=False, index_label='resultId', if_exists='replace')
conn.commit()

#inserto los datos en la base de datos con SQLite
drivers_df.to_sql('drivers', con=conn, index=False, index_label='driverId', if_exists='replace')
conn.commit()


query = 'SELECT * FROM drivers'
#almaceno en df
df_drivers= pd.read_sql(query, conn)
print(df_drivers.head())


#inserto los datos en la base de datos con SQLite
circuits_df.to_sql('circuits', con=conn, index=False, index_label='circuitId', if_exists='replace')
conn.commit()

#inserto los datos en la base de datos con SQLite
constructors_df.to_sql('constructors', con=conn, index=False, index_label='constructorId', if_exists='replace')
conn.commit()


