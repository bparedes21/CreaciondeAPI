import string
from tkinter.tix import INTEGER
import types
from venv import create
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

#users =Table("product",meta_data
#,column("IDArticulo", Integer)
#,column("Precio", Integer)
#,column("proveedor",string(255)
#,column("nombre",string(255)
#,column("precio_pesos", Integer)

#)

#crear tabla
#meta_data.create_all(engine)

#https://www.youtube.com/watch?v=6eVj33l5e9M&ab_channel=FaztCode