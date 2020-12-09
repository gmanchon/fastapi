
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


class Observation(BaseModel):
    content: dict  # str, list, dict, datetime


@app.post("/pred")
def make_pred(obs: Observation):
    return {"pred": obs}


# # test
#
# # uvicorn post:app
#
# observation = dict(content=dict(
#         key="value"
#     ))
#
# import requests
# url="http://127.0.0.1:8000/pred"
# requests.post(url, json=observation).json()
