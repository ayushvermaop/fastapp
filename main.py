from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def first():
    return {
        "message":"Welcome in FastApi pro app"
    }
