"""
ATS Service

Handles ATS Resume Analysis.

Author : AI Resume Optimizer
"""

from utils.ats import analyze_resume
from config.logging_config import setup_logger

logger = setup_logger()


class ATSService:

    @staticmethod
    def analyze(pdf_path: str) -> dict:

        logger.info("ATS Service Started")

        result = analyze_resume(pdf_path)

        logger.info("ATS Service Completed")

        return result