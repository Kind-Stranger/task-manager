FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY common/ /app/common/
ENV PYTHONPATH="/app/common:${PYTHONPATH}"
