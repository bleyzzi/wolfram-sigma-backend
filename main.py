from fastapi import FastAPI
from wolfram_sigma_backend.app.database.database import Base

app = FastAPI()


@app.get("/")
def hello():
    return "Hello world"
