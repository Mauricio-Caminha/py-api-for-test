# API RESTful em Python 3.13 com FastAPI

API RESTful desenvolvida em Python 3.13 utilizando FastAPI, com estrutura organizada em rotas, controllers e services.

## Estrutura do Projeto

```
src/
├── models/                 # Modelos Pydantic (schemas)
│   ├── __init__.py
│   └── schemas.py
├── routes/                 # Definição das rotas FastAPI
│   ├── __init__.py
│   ├── user_routes.py
│   ├── car_routes.py
│   ├── product_routes.py
│   └── order_routes.py
├── controllers/           # Lógica de controle das requisições
│   ├── __init__.py
│   ├── user_controller.py
│   ├── car_controller.py
│   ├── product_controller.py
│   └── order_controller.py
├── services/              # Lógica de negócio
│   ├── __init__.py
│   ├── user_service.py
│   ├── car_service.py
│   ├── product_service.py
│   └── order_service.py
└── tests/                 # Testes unitários
    └── services/
        ├── __init__.py
        ├── test_user_service.py
        ├── test_car_service.py
        ├── test_product_service.py
        └── test_order_service.py
main.py                    # Arquivo principal da aplicação
requirements.txt           # Dependências do projeto
```

## Serviços Disponíveis

### 1. Users (`/api/users`)
- `GET /api/users` - Lista todos os usuários
- `GET /api/users/{id}` - Busca usuário por ID
- `POST /api/users` - Cria novo usuário
- `PUT /api/users/{id}` - Atualiza usuário
- `DELETE /api/users/{id}` - Deleta usuário

### 2. Cars (`/api/cars`)
- `GET /api/cars` - Lista todos os carros
- `GET /api/cars/{id}` - Busca carro por ID
- `POST /api/cars` - Cria novo carro
- `PUT /api/cars/{id}` - Atualiza carro
- `DELETE /api/cars/{id}` - Deleta carro

### 3. Products (`/api/products`)
- `GET /api/products` - Lista todos os produtos
- `GET /api/products/{id}` - Busca produto por ID
- `POST /api/products` - Cria novo produto
- `PUT /api/products/{id}` - Atualiza produto
- `DELETE /api/products/{id}` - Deleta produto

### 4. Orders (`/api/orders`)
- `GET /api/orders` - Lista todos os pedidos
- `GET /api/orders/{id}` - Busca pedido por ID
- `POST /api/orders` - Cria novo pedido
- `PUT /api/orders/{id}` - Atualiza pedido
- `DELETE /api/orders/{id}` - Deleta pedido

## Instalação

1. Certifique-se de ter Python 3.13 instalado:
```bash
python --version
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Configure as variáveis de ambiente (opcional):
Crie um arquivo `.env` na raiz do projeto:
```
PORT=3000
```

6. Inicie o servidor:
```bash
python main.py
```

Ou usando uvicorn diretamente:
```bash
uvicorn main:app --reload --port 3000
```

## Testes

O projeto está configurado com pytest para testes unitários.

Para executar os testes:
```bash
pytest
```

Para executar os testes com cobertura:
```bash
pytest --cov=src --cov-report=html
```

Para executar os testes em modo verbose:
```bash
pytest -v
```

## Endpoints

- Health Check: `GET /health`
- Documentação interativa (Swagger): `GET /docs`
- Documentação alternativa (ReDoc): `GET /redoc`
- Base URL: `http://localhost:3000`

## Observações

- Os dados são armazenados em memória (listas), então serão perdidos ao reiniciar o servidor
- A estrutura está preparada para fácil integração com banco de dados
- Projeto totalmente tipado com Pydantic
- Configurado para testes unitários com pytest e pytest-asyncio
- Utiliza FastAPI para alta performance e documentação automática

## Tecnologias Utilizadas

- Python 3.13
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- pytest-asyncio

