
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app = FastAPI()


class Observation(BaseModel):
    content: dict  # str, list, dict, datetime


@app.post("/pred")
def create_city(obs: Observation):
    return {"pred": obs}


# # test
#
# observation = dict(content=dict(
#         key="value"
#     ))
#
# import requests
# url="http://127.0.0.1:8000/pred"
# requests.post(url, json=observation).json()
