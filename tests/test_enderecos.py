from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

def gerar_complemento_unico():
    """Gera um complemento único para cada endereço."""
    return f"Apto {uuid.uuid4().hex[:8]}"

def test_create_endereco():
    """Testa a criação de um novo endereço (POST)"""
    complemento_unico = gerar_complemento_unico()
    response = client.post("/enderecos", json={
        "cep": "12345-678",
        "logradouro": "Rua Exemplo",
        "complemento": complemento_unico,
        "bairro": "Centro",
        "cidade": "Florianópolis",
        "estado": "SC",
        "estadoSigla": "SC",
        "pais": "Brasil",
        "paisSigla": "BR"
    })

    assert response.status_code == 200
    assert "id" in response.json()


def test_get_endereco():
    """Testa a busca de um endereço por ID (GET)"""
    complemento_unico = gerar_complemento_unico()
    response_create = client.post("/enderecos", json={
        "cep": "12345-678",
        "logradouro": "Rua Exemplo",
        "complemento": complemento_unico,
        "bairro": "Centro",
        "cidade": "Florianópolis",
        "estado": "SC",
        "estadoSigla": "SC",
        "pais": "Brasil",
        "paisSigla": "BR"
    })

    endereco_id = response_create.json()['id']

    response_get = client.get(f"/enderecos/{endereco_id}")

    assert response_get.status_code == 200
    assert response_get.json()['id'] == endereco_id
    assert response_get.json()['cep'] == "12345-678"
    assert response_get.json()['complemento'] == complemento_unico


def test_listar_enderecos():
    """Testa a listagem de todos os endereços (GET)"""
    response = client.get("/enderecos")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_endereco():
    """Testa a atualização de um endereço existente (PUT)"""
    complemento_unico = gerar_complemento_unico()
    response_create = client.post("/enderecos", json={
        "cep": "12345-678",
        "logradouro": "Rua Exemplo",
        "complemento": complemento_unico,
        "bairro": "Centro",
        "cidade": "Florianópolis",
        "estado": "SC",
        "estadoSigla": "SC",
        "pais": "Brasil",
        "paisSigla": "BR"
    })

    endereco_id = response_create.json()['id']

    response_update = client.put(f"/enderecos/{endereco_id}", json={
        "cep": "98765-432",
        "logradouro": "Rua Atualizada",
        "complemento": "Casa 202",
        "bairro": "Centro",
        "cidade": "Florianópolis",
        "estado": "SC",
        "estadoSigla": "SC",
        "pais": "Brasil",
        "paisSigla": "BR"
    })

    assert response_update.status_code == 200
    assert response_update.json()['cep'] == "98765-432"
    assert response_update.json()['logradouro'] == "Rua Atualizada"
    assert response_update.json()['complemento'] == "Casa 202" # Garante que o complemento foi atualizado


def test_delete_endereco():
    """Testa a deleção de um endereço existente (DELETE)"""
    complemento_unico = gerar_complemento_unico()
    response_create = client.post("/enderecos", json={
        "cep": "12345-678",
        "logradouro": "Rua Exemplo",
        "complemento": complemento_unico,
        "bairro": "Centro",
        "cidade": "Florianópolis",
        "estado": "SC",
        "estadoSigla": "SC",
        "pais": "Brasil",
        "paisSigla": "BR"
    })

    endereco_id = response_create.json()['id']

    response_delete = client.delete(f"/enderecos/{endereco_id}")
    assert response_delete.status_code == 200

    response_get = client.get(f"/enderecos/{endereco_id}")
    assert response_get.status_code == 404