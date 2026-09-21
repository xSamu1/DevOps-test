from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message" : "Hello World"}

@app.get("/teste1")
async def funcaotest():
    return {"teste" : "Deu certo", "teste2": "Deu certo novamente, msg discord"}


def somar(a: float, b: float) -> float:
    return a + b


def eh_par(numero: int) -> bool:
    return numero % 2 == 0


def saudacao(nome: str) -> str:
    nome = nome.strip()
    if not nome:
        return "Ola, mundo!"
    return f"Ola, {nome}!"


def media(numeros: list[float]) -> float:
    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)


@app.get("/saudacao/{nome}")
async def saudacao_endpoint(nome: str):
    return {"mensagem": saudacao(nome)}
