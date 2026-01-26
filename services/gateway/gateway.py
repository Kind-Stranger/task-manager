import os
import requests

from flask import request, jsonify, render_template
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from common.app import ServiceApp

app = ServiceApp(__name__)
logger = app.service_logger

session = requests.Session()
retries = Retry(
    total=3,              # number of retries
    backoff_factor=0.5,   # exponential backoff factor
    status_forcelist=[500, 502, 503, 504]
)
adapter = HTTPAdapter(max_retries=retries)
session.mount("http://", adapter)
session.mount("https://", adapter)

SERVICE_PORT = int(os.environ["SERVICE_PORT"])

TASK_HOSTNAME = os.environ["TASK_HOSTNAME"]
TASK_ENDPOINT = os.environ["TASK_ENDPOINT"]
TASK_URL = f"http://{TASK_HOSTNAME}:{SERVICE_PORT}/"

USER_HOSTNAME = os.environ["USER_HOSTNAME"]
USER_ENDPOINT = os.environ["USER_ENDPOINT"]
USER_URL = f"http://{USER_HOSTNAME}:{SERVICE_PORT}/"


@app.route("/")
def index():
    return render_template("tasks.html")


@app.get("/all")
def get_everything():
    tasks = get_json(f"{TASK_URL}{TASK_ENDPOINT}")
    users = get_json(f"{USER_URL}{USER_ENDPOINT}")
    return jsonify({"tasks": tasks, "users": users})


@app.get("/tasks")
def get_tasks():
    return get_json(f"{TASK_URL}{TASK_ENDPOINT}")


@app.post("/tasks")
def new_task():
    data = request.json
    return session.post(f"{TASK_URL}{TASK_ENDPOINT}", json=data).json()


@app.post("/users")
def new_user():
    data = request.json
    return session.post(f"{USER_URL}{USER_ENDPOINT}", json=data).json()


def get_json(url: str):
    res = session.get(url)
    res.raise_for_status()
    return res.json()
