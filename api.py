import os
import time
import datetime

from fastapi import FastAPI

app = FastAPI()


# Test Root
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Test Environment Variables
@app.get("/message")
async def _():
    message = os.environ.get("message")
    return {"message": message}

# Test Date
@app.get("/date")
async def _():
    return {"message": datetime.datetime.now()}

# Test complex routes
@app.get("/complex/123/my")
async def _():
    return {"message": "I was hidden"}

# Test Path Parameter
@app.get("/items/{item_id}")
async def _(item_id):
    return {"message": item_id}

# Test Query Parameter
@app.get("/query")
async def _(**kwargs):
    return {"message": kwargs}

# Test Timeout
@app.get("/slow")
async def _():
    time.sleep(9)
    return {"message": "I take 9 seconds"}

# Test Post
@app.post("/login")
async def _(username, password):
    return {"username": username}

# Test Dummy Endpoint 1
@app.get("/dummy1")
async def _():
    return {"message": "Hello Dummy 1"}

# Test Dummy Endpoint 2
@app.get("/dummy2")
async def _():
    return {"message": "Hello Dummy 2"}

# Test Dummy Endpoint 3
@app.get("/dummy3")
async def _():
    return {"message": "Hello Dummy 3"}