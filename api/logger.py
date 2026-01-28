import logging
from logging.handlers import RotatingFileHandler


def setup_logger():
    logger = logging.getLogger("rag_api")
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(
        "logs/rag_api.log",
        maxBytes=5_000_000,
        backupCount=5,
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
