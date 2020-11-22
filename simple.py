from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"key": "value"}


@app.get("/hello/{name}")
def hello(name):
    return {"key": f"Hello, {name}!"}
