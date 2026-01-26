import logging
import os
import sys
import urllib.request
from flask import Blueprint, Response, jsonify
from typing import Literal

logger = logging.getLogger(__name__)


OkResponse = tuple[Response, Literal[200]]


bp = Blueprint("health", __name__)


@bp.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


def perform_health_check():
    """Checks the /health endpoint of the service running on the specified port."""
    port = os.getenv("SERVICE_PORT")
    if not port:
        logger.error("SERVICE_PORT environment variable is not set.")
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
