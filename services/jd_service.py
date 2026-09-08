"""
JD Matching Service
"""

from utils.jd_matcher import match_resume_with_jd
from config.logging_config import setup_logger

logger = setup_logger()


class JDService:

    @staticmethod
    def match(
        pdf_path: str,
        job_description: str
    ) -> dict:

        logger.info("JD Matching Started")

        result = match_resume_with_jd(
            pdf_path,
            job_description
        )

        logger.info("JD Matching Completed")

        return result