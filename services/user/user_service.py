import os
from flask import Flask, request, jsonify

app = Flask(__name__)

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
