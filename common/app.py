from flask import Flask, request, Response
from common.logging_setup import setup_logger
from common.health import bp


class ServiceApp(Flask):
    def __init__(self, service_name: str, *args, **kwargs): # type: ignore
        """Custom Flask app with integrated logging
        
        Args:
            service_name (str): Name of the service for logging purposes
        """
        super().__init__(service_name, *args, **kwargs) # type: ignore

        # Configure logging once
        self.service_logger = setup_logger(service_name)
        self.register_blueprint(bp)

        self.skip_paths = {"/health", "/favicon.ico"}

    #     # Register request logging hooks
    #     self.before_request(self._log_request)
    #     self.after_request(self._log_response)

    # def _skip_logging(self):
    #     """Determine if the current request should skip logging"""
    #     return any(request.path.startswith(p) for p in self.skip_paths)

    # def _log_request(self):
    #     """Log incoming request details"""
    #     self.service_logger.info(f"Incoming request: {request.method} {request.path}")

    # def _log_response(self, response: Response):
    #     """Log outgoing response details"""
    #     if request.path not in self.skip_paths:
    #         self.service_logger.info(
    #             f"Completed request: {request.method} {request.path} "
    #             f"-> {response.status_code}"
    #         )
    #     return response
