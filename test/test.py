from src.main import *


def test_root():
    assert root() == {"message" : "Hello World"}

def test_funcaotest():
    assert funcaotest() == {"teste" : "Deu certo", "teste2": "Deu certo novamente"}