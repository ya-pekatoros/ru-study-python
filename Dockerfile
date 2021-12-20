FROM python:3.9-slim as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
        curl

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py > get-poetry.py \
    && python get-poetry.py --version 1.1.12 \
    && rm get-poetry.py

ENV PATH $PATH:/root/.poetry/bin

RUN poetry config virtualenvs.create false
ENV PATH $PATH:/root/.poetry/bin

COPY pyproject.toml poetry.lock ./
RUN poetry install  --no-interaction --no-ansi

ADD . /app

CMD bash