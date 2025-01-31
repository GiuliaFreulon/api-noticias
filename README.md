# API de Notícias

## Visão Geral
- Este é um projeto de API de Notícias desenvolvido em Django e Django REST Framework
- A API permite a criação, leitura, atualização e exclusão de notícias, utilizando armazenamento de dados em memória
- O projeto possui 11 testes unitários
- O projeto está dockerizado para facilitar a configuração e a replicação

## Pré-requisitos
- Python 3.12
- Docker
- Docker Compose

## Instalação e Uso

### Clonar o Repositório
```bash
git clone https://github.com/GiuliaFreulon/api-noticias
cd api-noticias

### Configurar o Ambiente Virtual
```bash
python -m venv .venv
source .venv/bin/activate  # No Windows, use .venv\Scripts\activate
pip install -r requirements.txt

### Rodar a Aplicação
```bash
python manage.py runserver

## Endpoints
- **Listar todas as notícias**
<p>GET /noticias/

- **Obter uma notícia específica por ID**
<p>GET /noticias/{id}/

- **Criar uma nova notícia**
<p>POST /noticias/

- **Atualizar uma notícia existente**
<p>PUT /noticias/{id}/ 
<p>ou
<p>PATCH /noticias/{id}/

- **Remover uma notícia**
<p>DELETE /noticias/{id}/

## Rodar os testes
```bash
python manage.py test
