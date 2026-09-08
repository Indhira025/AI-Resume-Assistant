from pathlib import Path
import json

from config.logging_config import setup_logger
from utils.pdf_reader import extract_resume_text
from utils.prompt_loader import load_prompt
from utils.ollama_client import ask_ai

logger = setup_logger()


def rewrite_resume(resume_path: str, job_description: str = "") -> str:
    """
    Rewrite resume according to the job description.

    Supports PDF and DOCX input.
    Returns AI-generated resume text.
    """

    logger.info("Starting Resume Rewrite")

    extension = Path(resume_path).suffix.lower()

    # Extract resume text
    if extension == ".pdf":
        resume_text = extract_resume_text(resume_path)

    elif extension == ".docx":
        from docx import Document

        doc = Document(resume_path)
        resume_text = "\n".join(
            p.text for p in doc.paragraphs if p.text.strip()
        )

    else:
        raise ValueError("Only PDF and DOCX resumes are supported.")

    if not resume_text.strip():
        raise ValueError("Could not extract resume text.")

    logger.info("Resume extracted")

    # Load prompt
    prompt_template = load_prompt("rewrite_prompt.txt")

    prompt = prompt_template.format(
        resume=resume_text,
        job_description=job_description.strip()
        if job_description
        else "No job description provided."
    )

    logger.info("Rewrite prompt prepared")

    response = ask_ai(prompt)

    if not response:
        raise ValueError("AI returned an empty response.")

    logger.info("Resume rewritten successfully")

    return response.strip()