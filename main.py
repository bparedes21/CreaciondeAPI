#Python
from typing import Optional

#Pydantic
#from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body

#iniciamos FastApi
app = FastAPI()

#Esto se llama PathOperation decoration
@app.get("/")  
#Esto se llama Path Operation Function 
def home():  
	return { "mesaje" : "Hola mundo" }