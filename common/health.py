import logging
import os
import sys
import urllib.request
from flask import Response, jsonify, Flask
from typing import Callable, Literal

logger = logging.getLogger(__name__)


OkResponse = tuple[Response, Literal[200]]
OkResponseFunction = Callable[[], OkResponse]


def register_health(app: Flask, health_fn: OkResponseFunction | None = None):
    """Registers a generic /health endpoint on the given Flask app.

    Args:
        app: The Flask application instance.
        health_fn: An optional function to override the default health check behavior.
    """
    logger = logging.getLogger(app.import_name)
    logger.info("Registering /health endpoint")
    if health_fn is None:
        def default_health_fn() -> OkResponse:
            return jsonify({
                "status": "ok",
                "service": app.import_name
            }), 200
        health_fn = default_health_fn

    app.add_url_rule("/health", "health", health_fn, methods=["GET"])


def perform_health_check():
    """Checks the /health endpoint of the service running on the specified port."""
    port = os.getenv("FLASK_RUN_PORT")
    if not port:
        logger.error("FLASK_RUN_PORT environment variable is not set.")
        sys.exit(1)

    logger.info(f"Performing health check on port {port}")
    url = f"http://localhost:{port}/health"
    try:
        with urllib.request.urlopen(url) as response:
            if response.status != 200:
                logger.error(
                    f"Health check failed with status code: {response.status}")
                sys.exit(1)
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    perform_health_check()
