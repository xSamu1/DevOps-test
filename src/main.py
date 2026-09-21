from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message" : "Hello World"}

@app.get("/teste1")
async def funcaotest():
    return {"teste" : "Deu certo", "teste2": "Deu certo novamente, msg discord"}