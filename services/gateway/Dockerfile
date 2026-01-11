FROM task-manager-base:latest

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=gateway.py

CMD ["flask", "run"]
