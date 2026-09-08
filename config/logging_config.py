'''
import logging
from pathlib import Path

from config.settings import LOG_LEVEL

# Create the logs directory if it doesn't exist
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Log file path
LOG_FILE = LOG_DIR / "app.log"


def setup_logger() -> logging.Logger:
    """
    Configure and return the application logger.
    """

    logger = logging.getLogger("resume_optimizer")

    # Prevent duplicate handlers if setup_logger() is called multiple times
    if logger.hasHandlers():
        return logger

    logger.setLevel(LOG_LEVEL)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File handler
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger  '''

"""
Logging Configuration

Author : AI Resume Optimizer
"""

import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(
    exist_ok=True
)

LOG_FILE = LOG_DIR / "resume_optimizer.log"


def setup_logger():

    logger = logging.getLogger(
        "resume_optimizer"
    )

    if logger.handlers:
        return logger

    logger.setLevel(
        logging.INFO
    )

    formatter = logging.Formatter(

        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",

        "%Y-%m-%d %H:%M:%S"

    )

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    file_handler.setFormatter(
        formatter
    )

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(
        formatter
    )

    logger.addHandler(
        file_handler
    )

    logger.addHandler(
        console_handler
    )

    logger.propagate = False

    return logger