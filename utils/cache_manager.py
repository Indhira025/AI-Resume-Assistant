"""
Cache Manager

Handles reading and writing cache files.
"""

import json
from pathlib import Path

from config.logging_config import setup_logger

logger = setup_logger()


CACHE_FILE = Path("outputs/cache.json")


def load_cache() -> dict:
    """
    Load cache from disk.
    """

    if not CACHE_FILE.exists():
        return {}

    try:

        with open(CACHE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except Exception as error:

        logger.exception(error)

        return {}


def save_cache(data: dict) -> None:
    """
    Save cache to disk.
    """

    try:

        CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(CACHE_FILE, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    except Exception as error:

        logger.exception(error)