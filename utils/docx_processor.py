"""
DOCX Resume Processor
Handles DOCX resume reading and content replacement.
"""

from pathlib import Path

from docx import Document

from config.logging_config import setup_logger

logger = setup_logger()


def extract_docx_text(file_path: str) -> str:
    """Extract readable text from a DOCX file."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"DOCX file not found: {file_path}")

    document = Document(file_path)
    sections = []

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        if text:
            sections.append(text)

    # Extract table content as well
    for table in document.tables:
        for row in table.rows:
            row_text = " | ".join(
                cell.text.strip()
                for cell in row.cells
                if cell.text.strip()
            )

            if row_text:
                sections.append(row_text)

    text = "\n".join(sections).strip()

    if not text:
        raise ValueError("No readable text found in DOCX.")

    logger.info("DOCX text extracted successfully.")

    return text