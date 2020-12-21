from io import BytesIO

from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse


some_file_path = "/home/jugs/Downloads/message_broker_in_threading.mp4"
img_file = "/home/jugs/Downloads/IMG_20190506_185557.jpg"
app = FastAPI()


@app.get("/")
async def main():
    # file_like = open(some_file_path, mode="rb")
    # return StreamingResponse(file_like, media_type="video/mp4")
    image = BytesIO()
    img = image
    img.save()
    return FileResponse(img_file)
