from src.main import *
import pytest

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message" : "Hello World"}

@pytest.mark.asyncio
async def test_funcaotest():
    result = await funcaotest()
    assert result == {"teste": "Deu certo", "teste2": "Deu certo novamente, msg discord"}


@pytest.mark.parametrize(
    "a, b, esperado",
    [(2, 3, 5), (0, 0, 0), (-4, 4, 0), (2.5, 0.5, 3.0)],
)
def test_somar(a, b, esperado):
    assert somar(a, b) == esperado


@pytest.mark.parametrize("numero", [0, 2, 10, -8])
def test_eh_par_reconhece_par(numero):
    assert eh_par(numero) is True


@pytest.mark.parametrize("numero", [1, 7, -3])
def test_eh_par_reconhece_impar(numero):
    assert eh_par(numero) is False


def test_saudacao_com_nome():
    assert saudacao("Lucas") == "Ola, Lucas!"


def test_saudacao_ignora_espacos_em_volta():
    assert saudacao("   Lucas   ") == "Ola, Lucas!"


def test_saudacao_sem_nome_cumprimenta_o_mundo():
    assert saudacao("   ") == "Ola, mundo!"


def test_media_de_varios_numeros():
    assert media([2, 4, 6, 8]) == 5.0


def test_media_de_um_unico_numero():
    assert media([7]) == 7.0


def test_media_de_lista_vazia_nao_estoura():
    assert media([]) == 0.0


@pytest.mark.asyncio
async def test_saudacao_endpoint():
    result = await saudacao_endpoint("Lucas")
    assert result == {"mensagem": "Ola, Lucas!"}
