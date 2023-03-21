#Importación de las librerías necesarias.
from fastapi import FastAPI
from router.router import user
import pandas as pd
from pandasql import sqldf
from pydantic import BaseModel
from typing import Union
from fastapi import File, UploadFile

#le ponemos titulo
app = FastAPI()

app.include_router(user)

#http://127.0.0.1:8000


@app.get('/')
def index():
    return {'Mi primera API Mariana Tapia DTS-08'}

@app.get('items/{item_id}')
def read_item(item_id: int, q: Union [str, None] = None):
    return {'item_id': item_id, 'q' : q}





