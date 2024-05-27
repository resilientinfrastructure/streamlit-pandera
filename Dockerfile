FROM python:3.12-slim
# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9


ENV BACKEND_HOST=${BACKEND_HOST}

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install GDAL and Fiona system dependencies
RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

ARG INSTALL_DEV=false

COPY ./ /app

RUN bash -c "poetry install"

