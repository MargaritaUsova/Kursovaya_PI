from fastapi import FastAPI
from pydantic import BaseModel
from parser_gost import parser

class User_Input(BaseModel):
    doc : str


app = FastAPI()

@app.post("/parser")

def operate(input:User_Input):
    result = parser(input.doc)
    return result
