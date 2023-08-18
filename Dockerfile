FROM python:3.10-slim

COPY pyproject.toml /app/
WORKDIR /app

RUN \
    pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install
