# manage python version and buffering
FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

# install postgres dependencies
RUN apk --update add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq \
    # pillow dependencies
    jpeg-dev \
    zlib-dev

# create workdir
WORKDIR /code

# copy requirements
ADD requirements.txt /code/

# install dependecies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy projects
COPY . /code/
