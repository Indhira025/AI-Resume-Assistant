"""
Roadmap Generator

Generates a personalized learning roadmap
using the resume and target job role.

Author : AI Resume Optimizer
"""

from config.logging_config import setup_logger

from utils.pdf_reader import extract_resume_text
from utils.prompt_loader import load_prompt
from utils.ollama_client import ask_ai

logger = setup_logger()


def generate_learning_roadmap(
    pdf_path: str,
    target_role: str
) -> str:
    """
    Generate a personalized learning roadmap.

    Args:
        pdf_path (str):
            Resume PDF path.

        target_role (str):
            Desired job role.

    Returns:
        str:
            AI generated learning roadmap.
    """

    logger.info("Generating learning roadmap.")

    # -----------------------------
    # Extract Resume
    # -----------------------------

    resume = extract_resume_text(pdf_path)

    logger.info("Resume extracted.")

    # -----------------------------
    # Load Prompt
    # -----------------------------

    prompt = load_prompt(
        "roadmap_prompt.txt"
    )

    logger.info("Roadmap prompt loaded.")

    # -----------------------------
    # Prepare Prompt
    # -----------------------------

    final_prompt = prompt.format(
        resume=resume,
        target_role=target_role
    )

    logger.info("Prompt prepared.")

    # -----------------------------
    # AI Response
    # -----------------------------

    roadmap = ask_ai(final_prompt)

    logger.info("Roadmap generated successfully.")

    return roadmap.strip()