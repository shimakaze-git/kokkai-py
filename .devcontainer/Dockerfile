FROM python:3.10-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends --allow-unauthenticated \
    apt-utils \
    dialog \
    procps \
    git \
    lsb-release \
    gcc \
    build-essential \
    libmariadb-dev \
    && pip install --upgrade pip \
    && pip install --no-cache-dir \
    autopep8 flake8 isort pre-commit lizard tox \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
