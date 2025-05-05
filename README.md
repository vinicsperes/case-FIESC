# 📦 Case Prático - Desenvolvedor Full Stack - SENAI/SC (00942/2025)

Este projeto consiste em uma API REST desenvolvida com **Python + FastAPI** e banco de dados **PostgreSQL**, conforme os requisitos do processo seletivo para a vaga de Desenvolvedor Full Stack - Pleno.

---

## 🚀 Funcionalidades da API

A API permite **criar, listar, buscar, atualizar e deletar** endereços, com os seguintes atributos:

- `id`
- `cep`
- `logradouro`
- `complemento`
- `bairro`
- `cidade`
- `estado`
- `estadoSigla`
- `pais`
- `paisSigla`

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
git clone https://github.com/seu-usuario/caseFIESC.git
cd caseFIESC
```

2. Crie e ative o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

```bash
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
```

5. Execute a aplicação
```bash
uvicorn app.main:app --reload
```
Acesse: http://localhost:8000/docs para visualizar a documentação interativa via Swagger.

🧪 Rodando os testes
```bash
pytest
```

📁 Estrutura do Projeto
```pgsql
caseFIESC/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── routers/
│       └── enderecos.py
├── tests/
│   └── test_schemas.py
├── .env
├── requirements.txt
└── README.md
```

## 👨‍💻 Autor
Vinícius Peres