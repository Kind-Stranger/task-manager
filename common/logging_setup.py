import logging
from pythonjsonlogger.json import JsonFormatter


def setup_logger(service_name: str):
    """Setup JSON logger for a service

    Args:
        service_name (str): Name of the service

    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(service_name)
    logger.setLevel(logging.INFO)

    logHandler = logging.StreamHandler()
    formatter = JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s",
        json_indent=2,
        json_ensure_ascii=False
    )
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)

    return logger
