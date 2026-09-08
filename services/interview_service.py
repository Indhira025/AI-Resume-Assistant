"""
Interview Question Service
"""

from utils.interview_generator import generate_interview_questions
from config.logging_config import setup_logger

logger = setup_logger()


class InterviewService:

    @staticmethod
    def generate(
        pdf_path: str,
        role: str
    ) -> dict:

        logger.info("Interview Generation Started")

        result = generate_interview_questions(
            pdf_path,
            role
        )

        logger.info("Interview Generation Completed")

        return result