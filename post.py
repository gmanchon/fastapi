from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.post("/pred")
def make_pred(obs: dict):
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
