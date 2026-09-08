"""
PDF Reader Module

This module is responsible for:
1. Validating PDF files
2. Extracting text from PDF resumes
3. Logging every operation
"""

import pdfplumber

from config.logging_config import setup_logger
from utils.helpers import get_file_extension

logger = setup_logger()


def extract_resume_text(file_path: str) -> str:
    """
    Extract text from a resume PDF.
    """

    logger.info(f"Reading resume: {file_path}")

    extension = get_file_extension(file_path)

    if extension != "pdf":
        logger.error("Unsupported file format.")
        raise ValueError("Only PDF files are supported.")

    resume_text = ""

    try:

        with pdfplumber.open(file_path) as pdf:

            logger.info(f"Total Pages: {len(pdf.pages)}")

            for page_number, page in enumerate(pdf.pages, start=1):

                logger.info(f"Reading Page {page_number}")

                page_text = page.extract_text()

                if page_text:
                    resume_text += page_text + "\n"

    except Exception as error:

        logger.exception(error)
        raise

    if not resume_text.strip():

        logger.warning("Resume contains no readable text.")

        raise ValueError("No text found inside the PDF.")

    logger.info("Resume extraction completed successfully.")

    return resume_text.strip()