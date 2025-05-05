# 📦 Case Prático - Desenvolvedor Full Stack - SENAI/SC (00942/2025)

Este projeto consiste em uma API REST desenvolvida com **Python + FastAPI** e banco de dados **PostgreSQL**, conforme os requisitos do processo seletivo para a vaga de Desenvolvedor Full Stack - Pleno.

---

## 🚀 Funcionalidades da API

A API permite **criar, listar, buscar, atualizar e deletar** endereços, com os seguintes atributos:
 `id`, `cep`, `logradouro`, `complemento`, `bairro`, `cidade`, `estado`, `estadoSigla`, `pais` e `paisSigla`

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.12
- **Framework:** FastAPI
- **Servidor:** Uvicorn
- **ORM:** SQLAlchemy
- **Banco de Dados:** PostgreSQL
- **Validação de Dados:** Pydantic
- **Testes:** Pytest

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/vinicsperes/case-FIESC.git
cd case-FIESC
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## 🎲 Configuração do Banco de Dados

Este projeto utiliza PostgreSQL como banco de dados.

### 4.1 Criação do Banco
Você pode criar o banco com o seguinte comando no terminal, usando psql:

```bash
createdb case_fiesc
```
Ou acessando o PostgreSQL interativamente:

```bash
psql -U postgres
CREATE DATABASE case_fiesc;
```

Substitua postgres pelo seu usuário, se necessário.

### 4.2 Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

```bash
DATABASE_URL=postgresql://<usuario>:<senha>@localhost:5432/case_fiesc
```

Exemplo:
```bash
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/case_fiesc
```

### 4.3 Criação das Tabelas
Execute o script de criação de tabelas:

```bash
python create_tables.py
```

## Execute a aplicação
```bash
uvicorn app.main:app --reload
```
Acesse: http://localhost:8000/docs para visualizar a documentação interativa via Swagger.

## 🧪 Rodando os testes
```bash
pytest
```

## 👨‍💻 Autor
Vinícius Peres
