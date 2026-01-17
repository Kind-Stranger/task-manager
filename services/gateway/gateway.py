import os
import requests

from flask import Flask, request, jsonify
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from common.healthcheck import register_health
from common.logging_setup import setup_logger

session = requests.Session()
retries = Retry(
    total=3,              # number of retries
    backoff_factor=0.5,   # exponential backoff factor
    status_forcelist=[500, 502, 503, 504]
)
adapter = HTTPAdapter(max_retries=retries)
session.mount("http://", adapter)
session.mount("https://", adapter)

app = Flask(__name__)
logger = setup_logger(app.import_name)
register_health(app)

TASK_URL = os.getenv("TASK_URL")
TASK_ENDPOINT = os.getenv("TASK_ENDPOINT")
USER_URL = os.getenv("USER_URL")
USER_ENDPOINT = os.getenv("USER_ENDPOINT")


@app.get("/all")
def get_everything():
    tasks = session.get(f"{TASK_URL}{TASK_ENDPOINT}").json()
    users = session.get(f"{USER_URL}{USER_ENDPOINT}").json()
    return jsonify({"tasks": tasks, "users": users})


@app.post("/new-task")
def new_task():
    data = request.json
    return session.post(f"{TASK_URL}{TASK_ENDPOINT}", json=data).json()


@app.post("/new-user")
def new_user():
    data = request.json
    return session.post(f"{USER_URL}{USER_ENDPOINT}", json=data).json()
