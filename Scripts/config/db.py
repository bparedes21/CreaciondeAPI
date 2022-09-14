from sqlalchemy import create_engine, MetaData
import sqlalchemy
#necesita url usuario, contraseña, servidor donde esta alojado
# el puerto y la base de datos
#otras bibliotecas como pymysql
#engine = sqlalchemy.create_engine('mysql://user:password@server')
#engine.execute("CREATE DATABASE dbraces") #create db
#engine.execute("USE dbraces") # 
# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD

# DEFINE THE DATABASE CREDENTIALS
user = 'root'
password = 'password'
host = '127.0.0.1'
port = 8000
database = 'dbraces'


engine = create_engine(url="mysql+pymysql://user:password@host:port/database")
conect=engine.conect()
meta_data=MetaData()