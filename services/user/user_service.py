import os
from flask import Flask, request, jsonify

from common.healthcheck import register_health
from common.logging_setup import setup_logger

app = Flask(__name__)
logger = setup_logger(app.import_name)
register_health(app)

USER_ENDPOINT = os.getenv("USER_ENDPOINT")

users = []


@app.get(USER_ENDPOINT)
def get_users():
    return jsonify(users)


@app.post(USER_ENDPOINT)
def add_user():
    data = request.json
    users.append({"id": len(users)+1, "name": data["name"]})
    return jsonify({"status": "ok"}), 201
