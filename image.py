
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from starlette.responses import StreamingResponse

import io


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.post("/return_file")
def image_endpoint():
    """
    returns an image
    """

    # read file
    with open("image.png", "rb") as file:
        image_bytes = file.read()

    return StreamingResponse(io.BytesIO(image_bytes), media_type="image/png")
