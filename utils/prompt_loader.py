"""
Prompt Loader

Loads prompt templates from the prompts folder.
"""

from pathlib import Path

from config.logging_config import setup_logger

logger = setup_logger()

PROMPT_FOLDER = Path("prompts")


def load_prompt(file_name: str) -> str:
    """
    Load a prompt template from the prompts directory.

    Args:
        file_name (str): Name of the prompt file.

    Returns:
        str: Prompt template.
    """

    prompt_path = PROMPT_FOLDER / file_name

    logger.info(f"Loading prompt: {prompt_path}")

    if not prompt_path.exists():
        logger.error(f"Prompt not found: {prompt_path}")
        raise FileNotFoundError(f"{prompt_path} does not exist.")

    with open(prompt_path, "r", encoding="utf-8") as file:
        prompt = file.read()

    logger.info("Prompt loaded successfully.")

    return prompt