import os
from flask import Flask, request, jsonify

from common.healthcheck import register_health


app = Flask(__name__)
register_health(app)

TASK_ENDPOINT = os.getenv("TASK_ENDPOINT")

tasks = []


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
