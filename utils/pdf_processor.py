"""
PDF Resume Processor
Handles PDF resume text extraction.
"""

from pathlib import Path

import pdfplumber

from config.logging_config import setup_logger

logger = setup_logger()


def extract_pdf_text(file_path: str) -> str:
    """Extract readable text from a PDF."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    text_parts = []

    with pdfplumber.open(file_path) as pdf:

        logger.info(f"PDF pages: {len(pdf.pages)}")

        for page_number, page in enumerate(pdf.pages, start=1):

            logger.info(f"Reading PDF page {page_number}")

            text = page.extract_text()

            if text:
                text_parts.append(text)

    text = "\n".join(text_parts).strip()

    if not text:
        raise ValueError(
            "No readable text found in PDF. "
            "The PDF may contain scanned images."
        )

    logger.info("PDF text extracted successfully.")

    return text