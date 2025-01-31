# API de Notícias

## Visão Geral
- Este é um projeto de API de Notícias desenvolvido em Django e Django REST Framework
- A API permite a criação, leitura, atualização e exclusão de notícias, utilizando armazenamento de dados em memória
- O projeto possui 11 testes unitários
- O projeto está dockerizado para facilitar a configuração e a replicação

## Tecnologias Utilizadas
- Python
- Django
- Django REST Framework
- Docker
- Docker Compose

## Instalação e Uso

### Clonar o Repositório
```bash
git clone https://github.com/GiuliaFreulon/api-noticias
cd api-noticias
```

### Configurar o Ambiente Virtual
```bash
python -m venv .venv
source .venv/bin/activate  # No Windows, use .venv\Scripts\activate
pip install -r requirements.txt
```

### Rodar a Aplicação
```bash
python manage.py runserver
```

### Testar a API
<p>É possível testar a API utilizando ferramentas como Postman ou cURL.
<p>No Postman, por exemplo:

- **Listar todas as notícias**
<p>GET http://localhost:8000/api/noticias/

- **Obter uma notícia específica por ID**
<p>GET http://localhost:8000/api/noticias/<ID>

- **Criar uma nova notícia**
<p>POST http://localhost:8000/api/noticias/
<p>No Body um JSON:
  {
      "titulo": "Título da Notícia",
      "conteudo": "Conteúdo da Notícia",
      "autor": "Autor da Notícia"
  }

- **Atualizar uma notícia existente**
<p>PUT "Content-Type: application/json" -d '{"titulo": "Atualizado", "conteudo": "Conteúdo Atualizado", "autor": "Autor"}' http://localhost:8000/api/noticias/<ID>
<p>ou
<p>PATCH "Content-Type: application/json" -d '{"titulo": "Atualizado", "conteudo": "Conteúdo Atualizado", "autor": "Autor"}' http://localhost:8000/api/noticias/<ID>

<p>No Body um JSON:
  {
      "titulo": "Título da Notícia Atualizada",
      "conteudo": "Conteúdo da Notícia Atualizada",
      "autor": "Autor da Notícia Atualizada"
  }

- **Remover uma notícia**
<p>DELETE http://localhost:8000/api/noticias/<ID>

### Rodar os testes
```bash
python manage.py test
```

## Dockerização
### Construir imagem Docker
```bash
docker-compose build
```
### Rodar os Contêineres
```bash
docker-compose up
```

<p>A aplicação estará disponível em http://localhost:8000/api/noticias/
