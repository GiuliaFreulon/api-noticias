FROM python:3.12-slim

WORKDIR /app

# Dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Código
COPY . /app/

# Variáveis de ambiente
ENV DJANGO_SETTINGS_MODULE=noticias_api.settings

# Porta exposta
EXPOSE 8000

# Rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]