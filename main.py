from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return{"Message":"welcome to my first aPi"}

@app.post('/')
def create():
    return{"Message":"welcome to 2024"}
