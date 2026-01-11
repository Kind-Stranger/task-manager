import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TASK_URL = os.getenv("TASK_URL")
TASK_ENDPOINT = os.getenv("TASK_ENDPOINT")
USER_URL = os.getenv("USER_URL")
USER_ENDPOINT = os.getenv("USER_ENDPOINT")


@app.get("/all")
def get_everything():
    tasks = requests.get(f"{TASK_URL}{TASK_ENDPOINT}").json()
    users = requests.get(f"{USER_URL}{USER_ENDPOINT}").json()
    return jsonify({"tasks": tasks, "users": users})


@app.post("/new-task")
def new_task():
    data = request.json
    return requests.post(f"{TASK_URL}{TASK_ENDPOINT}", json=data).json()


@app.post("/new-user")
def new_user():
    data = request.json
    return requests.post(f"{USER_URL}{USER_ENDPOINT}", json=data).json()
