from fastapi import FastAPI
from pydantic import BaseModel
from parser_gost import parser

class Input(BaseModel):
    document : str 

app = FastAPI()

@app.post("/parser")

def operate(iinput:Input):
    result = parser(iinput.document)
    return result


