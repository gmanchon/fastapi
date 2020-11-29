from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"key": "value"}


@app.get("/predict")
def create_fare(a, b, c):
    return {"key": a + b + c}


@app.get("/hello/{name}")
def hello(name):
    return {"key": f"Hello, {name}!"}
