import os
import requests

from flask import Flask, request, jsonify
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from common.health import bp as health_blueprint
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
app.register_blueprint(health_blueprint)

FLASK_RUN_PORT = os.getenv("FLASK_RUN_PORT")
TASK_HOSTNAME = os.getenv("TASK_HOSTNAME")
TASK_ENDPOINT = os.getenv("TASK_ENDPOINT")
TASK_URL = f"http://{TASK_HOSTNAME}:{FLASK_RUN_PORT}/"
USER_HOSTNAME = os.getenv("USER_HOSTNAME")
USER_ENDPOINT = os.getenv("USER_ENDPOINT")
USER_URL = f"http://{USER_HOSTNAME}:{FLASK_RUN_PORT}/"


@app.get("/all")
def get_everything():
    tasks = getJson(f"{TASK_URL}{TASK_ENDPOINT}")
    users = getJson(f"{USER_URL}{USER_ENDPOINT}")
    return jsonify({"tasks": tasks, "users": users})


@app.post("/new-task")
def new_task():
    data = request.json
    return session.post(f"{TASK_URL}{TASK_ENDPOINT}", json=data).json()


@app.post("/new-user")
def new_user():
    data = request.json
    return session.post(f"{USER_URL}{USER_ENDPOINT}", json=data).json()


def get_json(url: str):
    res = session.get(url)
    res.raise_for_status()
    return res.json()