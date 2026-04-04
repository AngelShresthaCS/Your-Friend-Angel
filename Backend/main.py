from fastapi import FastAPI
import math
import random

app = FastAPI()

@app.get("/")
async def root():
    a = random.random()
    if a > 0.5:
        value = "Less that 0.5"
    else:
        value = "Greater than 0.5"
    return {"status": "The Web API is running.", "value": value}

