import os
from gunicorn.glogging import Logger

host = os.environ["SERVICE_HOST"]
port = os.environ["SERVICE_PORT"]
bind = f"{host}:{port}"
workers = 4
threads = 2
timeout = 30

accesslog = "-"
errorlog = "-"


class FilteredGunicornLogger(Logger):
    """Centralised Gunicorn logger with request filtering.
    """

    FILTERED_PATHS = {"/health", "/ready", "/live"}

    def access(self, resp, req, environ, request_time):  # type: ignore
        if req.path in self.FILTERED_PATHS:
            return
        super().access(resp, req, environ, request_time)

logger_class = FilteredGunicornLogger
