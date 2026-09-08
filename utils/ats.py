from config.logging_config import setup_logger
from utils.pdf_reader import extract_resume_text
from utils.prompt_loader import load_prompt
from utils.ollama_client import ask_ai
from utils.json_parser import parse_json

logger = setup_logger()


def analyze_resume(pdf_path: str) -> dict:

    logger.info("Starting ATS analysis.")

    resume_text = extract_resume_text(pdf_path)

    logger.info("Resume text extracted.")

    prompt = load_prompt("ats_prompt.txt")

    logger.info("ATS prompt loaded.")

    final_prompt = prompt.format(
        resume=resume_text
    )

    logger.info("Prompt prepared.")

    MAX_RETRIES = 2

    for attempt in range(MAX_RETRIES):

        ai_response = ask_ai(final_prompt)

        try:

            result = parse_json(
                ai_response,
                response_type="ats"
            )

            logger.info("ATS analysis completed.")

            return result

        except Exception:

            logger.warning(
                f"Retry {attempt + 1} due to invalid AI response."
            )

    raise ValueError(
        "Unable to obtain a valid AI response after multiple attempts."
    )