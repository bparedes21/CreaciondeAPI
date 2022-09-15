import pymysql
import pymysql.cursors

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
host = "127.0.0.1"
port = "8000"
database = 'dbraces'

#https://programmerclick.com/article/9843531918/
con = pymysql.connect(host,
        user,
        password,
        database ,
    )
                                   
try:
# Create a cursor object
    cursorObject= con.cursor()                                     
    # SQL query string
    sqlQuery= "CREATE TABLE Employee(IDArticulo int, Precio int, proveedor varchar(32), nombre varchar(32), precio_pesos int)"  
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)
    # SQL query string
    sqlQuery = "show tables"   
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)
    #Fetch all the rows
    rows = cursorObject.fetchall()
    for row in rows:
        print(row)

except Exception as e:

    print("Exeception occured:{}".format(e))

finally:

    con.close()

#engine = create_engine(url="mysql+pymysql://user:password@host:port/database")
#conect=engine.conect()
#meta_data=MetaData()

#users =Table("product",meta_data,column("IDArticulo", Integer),column("Precio", Integer),column("proveedor",string(255)),column("nombre",string(255),column("precio_pesos", Integer)))

#crear tabla
#meta_data.create_all(engine)