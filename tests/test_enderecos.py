from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_endereco():
    """Testa a criação de um novo endereço (POST)"""
    response = client.post("/enderecos", json={
        "cep": "12345-678",
        "logradouro": "Rua Exemplo",
        "complemento": "Apto 101",
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
    response_create = client.post("/enderecos", json={
        "cep": "12345-678",
        "logradouro": "Rua Exemplo",
        "complemento": "Apto 101",
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

def test_listar_enderecos():
    """Testa a listagem de todos os endereços (GET)"""
    response = client.get("/enderecos")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_endereco():
    """Testa a atualização de um endereço existente (PUT)"""
    response_create = client.post("/enderecos", json={
        "cep": "12345-678",
        "logradouro": "Rua Exemplo",
        "complemento": "Apto 101",
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

def test_delete_endereco():
    """Testa a deleção de um endereço existente (DELETE)"""
    response_create = client.post("/enderecos", json={
        "cep": "12345-678",
        "logradouro": "Rua Exemplo",
        "complemento": "Apto 101",
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
    #endereço não deve ser encontrado após a deleção
    assert response_get.status_code == 404  
