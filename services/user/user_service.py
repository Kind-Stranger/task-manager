import os
from flask import request, jsonify

from common.app import ServiceApp

app = ServiceApp(__name__)
logger = app.service_logger

USER_ENDPOINT = os.environ["USER_ENDPOINT"]
SERVICE_PORT = os.environ["SERVICE_PORT"]

users = []


@app.get(USER_ENDPOINT)
def get_users():
    return jsonify(users)


@app.post(USER_ENDPOINT)
def add_user():
    data = request.json
    users.append({"id": len(users)+1, "name": data["name"]})
    return jsonify({"status": "ok"}), 201
