"""
Prompt Builder Utility
Loads prompt templates and fills placeholders dynamically.
"""

from typing import Any

from config.logging_config import setup_logger
from utils.prompt_loader import load_prompt

logger = setup_logger()


def build_prompt(prompt_name: str, **kwargs: Any) -> str:
    """Load a prompt template and replace its placeholders."""

    logger.info(f"Building prompt: {prompt_name}")

    template = load_prompt(prompt_name)

    try:
        prompt = template.format(**kwargs)

        logger.info("Prompt built successfully.")
        return prompt

    except KeyError as error:
        logger.exception(error)
        raise ValueError(f"Missing prompt placeholder: {error}") from error

    except Exception as error:
        logger.exception(error)
        raise ValueError(f"Failed to build prompt: {error}") from error


def preview_prompt(prompt_name: str, **kwargs: Any) -> str:
    """Build and return a prompt for debugging/preview."""

    prompt = build_prompt(prompt_name, **kwargs)

    logger.info("Prompt preview generated.")
    return prompt


def validate_prompt(prompt: str) -> bool:
    """Validate a prompt before sending it to the AI model."""

    if not isinstance(prompt, str) or not prompt.strip():
        logger.error("Prompt is empty.")
        return False

    if len(prompt.strip()) < 20:
        logger.warning("Prompt is too short.")
        return False

    logger.info("Prompt validation successful.")
    return True


def prepare_prompt(prompt_name: str, **kwargs: Any) -> str:
    """Build and validate a prompt."""

    prompt = build_prompt(prompt_name, **kwargs)

    if not validate_prompt(prompt):
        raise ValueError("Prompt validation failed.")

    return prompt