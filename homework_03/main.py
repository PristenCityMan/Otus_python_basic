from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Home!"}


@app.get("/ping/")
async def home():
    return {"message": "pong"}
