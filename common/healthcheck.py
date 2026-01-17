from flask import Response, jsonify, Flask
from typing import Callable, Literal

OkResponse = tuple[Response, Literal[200]]
OkResponseFunction = Callable[[], OkResponse]


def register_health(app: Flask, health_fn: OkResponseFunction | None = None):
    """Registers a generic /health endpoint on the given Flask app.

    Args:
        app: The Flask application instance.
        health_fn: An optional function to override the default health check behavior.
    """
    if health_fn is None:
        def default_health_fn() -> OkResponse:
            return jsonify({
                "status": "ok",
                "service": app.import_name
            }), 200
        health_fn = default_health_fn

    app.add_url_rule("/health", "health", health_fn, methods=["GET"])
