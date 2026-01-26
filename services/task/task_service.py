import os
from flask import request, jsonify

from common.app import ServiceApp

app = ServiceApp(__name__)
logger = app.service_logger

TASK_ENDPOINT = os.environ["TASK_ENDPOINT"]
SERVICE_PORT = os.environ["SERVICE_PORT"]

tasks = [{"id": 1, "title": "Sample Task", "details": "This is a sample task"}] # type: ignore


@app.get(TASK_ENDPOINT)
def get_tasks():
    return jsonify(tasks)


@app.post(TASK_ENDPOINT)
def add_task():
    data = request.json
    tasks.append({"id": len(tasks)+1,
                  "title": data["title"],
                  "details": data.get("details")})
    return jsonify({"status": "ok"}), 201
