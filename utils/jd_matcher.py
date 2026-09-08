from config.logging_config import setup_logger

from utils.pdf_reader import extract_resume_text
from utils.prompt_loader import load_prompt
from utils.ollama_client import ask_ai
from utils.json_parser import parse_json

logger = setup_logger()


def match_resume_with_jd(
        pdf_path: str,
        job_description: str
) -> dict:

    logger.info("Starting JD Matching")

    resume = extract_resume_text(pdf_path)

    logger.info("Resume extracted")

    prompt = load_prompt(
        "jd_match_prompt.txt"
    )

    logger.info("JD prompt loaded")

    final_prompt = prompt.format(

        resume=resume,

        job_description=job_description

    )

    logger.info("Prompt prepared")

    response = ask_ai(final_prompt)

    result = parse_json(
        response,
        response_type="jd"
    )

    logger.info("JD Matching completed")

    return result