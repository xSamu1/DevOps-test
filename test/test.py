from src.main import *
import pytest

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message" : "Hello World"}

@pytest.mark.asyncio
async def test_funcaotest():
    result = await funcaotest()
    assert result == {"teste" : "Deu certo", "teste2": "Deu certo novamente"}