from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def first():
    return {
        "message":"Welcome in FastApi pro app"
    }


@app.get("/1")
def f1():
    return {"message":"one1"}