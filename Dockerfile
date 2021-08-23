# define a imagem base
FROM python:3.9-alpine

# evita que a saída do python no terminal seja bufferizada
ENV PYTHONUNBUFFERED 1

# instalar dependências do postgres
RUN apk --update add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq \
    # dependências do pillow
    jpeg-dev \
    zlib-dev

# cria o diretório de trabalho
WORKDIR /code

# as instruções ADD, COPY, CMD, ENTRYPOINT ou RUN serão executadas no diretório de trabalho definido anteriormente

# copia o projeto para o diretório de trabalho
COPY . /code/

# atualizar o pip e instalar as dependências do projeto
RUN pip install --upgrade pip
RUN pip install -r requirements/dev-requirements.txt
