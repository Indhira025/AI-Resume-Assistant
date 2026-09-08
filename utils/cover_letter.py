from config.logging_config import setup_logger

from utils.pdf_reader import extract_resume_text
from utils.prompt_loader import load_prompt
from utils.ollama_client import ask_ai

logger = setup_logger()


def generate_cover_letter(
    pdf_path: str,
    company: str,
    job_role: str,
    job_description: str
) -> str:
    """
    Generate a professional cover letter using AI.
    """

    logger.info("Starting Cover Letter Generation")

    resume = extract_resume_text(pdf_path)

    logger.info("Resume extracted successfully")

    prompt = load_prompt(
        "cover_letter_prompt.txt"
    )

    logger.info("Prompt loaded successfully")

    final_prompt = prompt.format(
        resume=resume,
        company=company,
        job_role=job_role,
        job_description=job_description
    )

    logger.info("Prompt prepared")

    response = ask_ai(final_prompt)

    logger.info("Cover Letter Generated")

    return response