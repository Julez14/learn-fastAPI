from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Welcome to FastAPI!"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """Greet someone by name."""
    return {"message": f"Hello {name}!"}
