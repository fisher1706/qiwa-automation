FROM python:3.10-slim

RUN apt update && apt install -y npm
RUN npm install -g @testmo/testmo-cli

COPY pyproject.toml /app/
WORKDIR /app

RUN \
    pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install
