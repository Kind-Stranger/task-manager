FROM task-manager-base:latest

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=user_service.py

CMD ["flask", "run"]