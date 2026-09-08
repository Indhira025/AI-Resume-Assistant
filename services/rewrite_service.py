"""
Resume Rewrite Service
"""

from utils.resume_rewriter import rewrite_resume
from config.logging_config import setup_logger

logger = setup_logger()


class RewriteService:

    @staticmethod
    def rewrite(pdf_path: str) -> str:

        logger.info("Resume Rewrite Started")

        result = rewrite_resume(pdf_path)

        logger.info("Resume Rewrite Completed")

        return result