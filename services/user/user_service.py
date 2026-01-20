import os
from flask import Flask, request, jsonify

from common.health import bp as health_blueprint
from common.logging_setup import setup_logger

app = Flask(__name__)
logger = setup_logger(app.import_name)
app.register_blueprint(health_blueprint)

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
