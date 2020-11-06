import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/message")
async def message():
    message = os.environ.get("message")
    return {"message": message}