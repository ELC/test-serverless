import os
import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/message")
async def message():
    message = os.environ.get("message")
    return {"message": message}

@app.get("/slow")
async def message():
    time.sleep(10)
    return {"message": "I take 10 seconds"}