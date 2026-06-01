# Minecraft Notes

Projeto full-stack demo com tema Minecraft que inclui:

- **Backend** em Flask com organização por Blueprints
- **API documentada** via OpenAPI/Swagger
- **Frontend** desktop em Flet consumindo a API
- **Landing page** estática em HTML + Tailwind CSS

## Tecnologias usadas

- Python 3.x
- Flask
- Pydantic
- Requests
- Flet
- Tailwind CSS

## Estrutura do projeto

- `backend/` - código do servidor Flask
  - `backend/app.py` - cria o app Flask, registra blueprint e expõe Swagger UI
  - `backend/notes/routes.py` - endpoints da API de notas
- `flet_app.py` - aplicação cliente em Flet que lista notas e envia novas notas
- `landing/index.html` - página estática de apresentação do projeto
- `requirements.txt` - dependências do projeto

## Funcionalidades

### Backend

- `GET /api/notes/` - retorna a lista de notas
- `GET /api/notes/<id>` - retorna uma nota específica
- `POST /api/notes/` - cria uma nova nota com validação Pydantic

### Frontend Flet

- Lista as notas retornadas pelo endpoint `GET /api/notes/`
- Formulário para criar uma nota via `POST /api/notes/`
- Feedback direto na UI para sucesso ou erro

### Landing Page

- Página estática com tema Minecraft
- Instruções de execução
- Cards de apresentação do projeto

## Instalação e execução

1. Abra o terminal na pasta do projeto
2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```powershell
python -m venv .venv
.venv\Scripts\activate
```

3. Instale as dependências

```powershell
pip install -r requirements.txt
```

4. Inicie o backend Flask

```powershell
python -m backend.app
```

5. Abra o Swagger para documentação da API

- `http://127.0.0.1:5000/apidocs`

6. Inicie o frontend Flet em outra janela de terminal

```powershell
python flet_app.py
```

7. Abra a landing page no navegador

- Abra o arquivo `landing/index.html`

## Observações

- O projeto usa armazenamento em memória em vez de banco de dados, então as notas são reiniciadas a cada execução.
- Se o Flet apresentar problemas com dependências, tente usar Python 3.10 ou 3.11.
- O Swagger está implementado usando um `swagger.json` gerado no backend e uma interface simples carregada em `/apidocs`.

## Commit e repositório

O projeto foi inicializado e enviado para o repositório GitHub:

https://github.com/carlostakeshita/LDW---Aplica-o-Full-Stack-com-Flask-e-Flet.git

## Como testar rapidamente

- Acesse `http://127.0.0.1:5000/apidocs` para ver os endpoints documentados
- Use o cliente Flet para criar notas e verificar a listagem em tempo real
- Abra `landing/index.html` para visualizar a página estática de apresentação
