FROM python:3.7.3-stretch

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

# NOTE: Não que isso esteja errado, mas eu prefiro que o Dockerfile apenas monte a maquina, não precisa rodar nada.
#ENTRYPOINT ["/app/django_start.sh"]