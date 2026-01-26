FROM task-manager-base:latest

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-c", "/opt/platform/gunicorn/gunicorn.conf.py", "user_service:app"]
