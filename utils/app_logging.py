import logging
import sys

import json_logging


def init_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    file_handler = logging.handlers.RotatingFileHandler(filename='my-pub-ip.log', maxBytes=5000000, backupCount=10)
    logger.addHandler(file_handler)
    return logger
