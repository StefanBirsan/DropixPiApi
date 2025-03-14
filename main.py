from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="FastAPI with Firebase",
    description="A simple FastAPI app with Firebase",
    docs_url="/",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post('/signup')
async def create_an_account():
    pass


@app.post('/login')
async def login():
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
