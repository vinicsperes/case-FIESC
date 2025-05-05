import pytest
from pydantic import ValidationError
from app.schemas import EnderecoBase


def test_cep_valido_sem_hifen():
    endereco = EnderecoBase(
        cep="12345678",
        logradouro="Rua A",
        complemento="Apto 101",
        bairro="Centro",
        cidade="Florianópolis",
        estado="Santa Catarina",
        estadoSigla="SC",
        pais="Brasil",
        paisSigla="BR"
    )
    assert endereco.cep == "12345678"


def test_cep_valido_com_hifen():
    endereco = EnderecoBase(
        cep="12345-678",
        logradouro="Rua B",
        complemento="Casa",
        bairro="Trindade",
        cidade="Florianópolis",
        estado="Santa Catarina",
        estadoSigla="SC",
        pais="Brasil",
        paisSigla="BR"
    )
    assert endereco.cep == "12345-678"


def test_cep_invalido_formato_curto():
    with pytest.raises(ValidationError):
        EnderecoBase(
            cep="1234-567",
            logradouro="Rua C",
            complemento="",
            bairro="Estreito",
            cidade="Florianópolis",
            estado="Santa Catarina",
            estadoSigla="SC",
            pais="Brasil",
            paisSigla="BR"
        )


def test_cep_invalido_com_letra():
    with pytest.raises(ValidationError):
        EnderecoBase(
            cep="12a45-678",
            logradouro="Rua D",
            complemento="",
            bairro="Kobrasol",
            cidade="São José",
            estado="Santa Catarina",
            estadoSigla="SC",
            pais="Brasil",
            paisSigla="BR"
        )
