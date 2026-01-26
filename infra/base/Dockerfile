FROM python:3.12-slim

WORKDIR /app

COPY infra/base/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY common/ /app/common/
ENV PYTHONPATH=/app/common:$PYTHONPATH

COPY infra/base/gunicorn.conf.py /opt/platform/gunicorn/gunicorn.conf.py

# No-op to prevent base container running
CMD ["true"]
