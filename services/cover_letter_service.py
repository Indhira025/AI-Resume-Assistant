"""
Cover Letter Service
"""

from utils.cover_letter import generate_cover_letter
from config.logging_config import setup_logger

logger = setup_logger()


class CoverLetterService:

    @staticmethod
    def generate(
        pdf_path: str,
        company: str,
        role: str,
        jd: str
    ) -> str:

        logger.info("Cover Letter Started")

        result = generate_cover_letter(
            pdf_path,
            company,
            role,
            jd
        )

        logger.info("Cover Letter Completed")

        return result