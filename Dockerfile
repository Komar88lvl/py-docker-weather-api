FROM python:3.12-slim
LABEL maintainer="djsv91@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "main.py"]
