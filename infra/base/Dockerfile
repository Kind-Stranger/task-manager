FROM python:3.12-slim

WORKDIR /app

COPY infra/base/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY common/ /app/common/
ENV PYTHONPATH=/app/common:$PYTHONPATH

# No-op to prevent base container running
CMD ["true"]
