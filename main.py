from fastapi import FastAPI
import uvicorn
from app import firebase, rtdb

app = FastAPI(
    title="FastAPI with Firebase",
    description="A simple FastAPI app with Firebase",
    docs_url="/",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/awb')
async def get_qr():
    box_data = rtdb.child("BOX").get().val()
    uris = [f"{field}" for field in box_data]
    return {"uris": uris}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
