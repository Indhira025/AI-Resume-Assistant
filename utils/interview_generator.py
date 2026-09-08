from config.logging_config import setup_logger
from utils.pdf_reader import extract_resume_text
from utils.prompt_loader import load_prompt
from utils.ollama_client import ask_ai
from utils.json_parser import parse_json

logger = setup_logger()

def generate_interview_questions(
    pdf_path: str,
    job_role: str
) -> dict:

    logger.info("Generating Interview Questions")

    resume = extract_resume_text(pdf_path)

    prompt = load_prompt(
        "interview_prompt.txt"
    )

    final_prompt = prompt.format(
        resume=resume,
        job_role=job_role
    )

    response = ask_ai(final_prompt)

    return parse_json(
        response,
        response_type="interview"
    )