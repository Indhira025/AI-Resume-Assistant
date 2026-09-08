"""
Learning Roadmap Service
"""

from utils.roadmap_generator import generate_learning_roadmap
from config.logging_config import setup_logger

logger = setup_logger()


class RoadmapService:

    @staticmethod
    def generate(
        pdf_path: str,
        role: str
    ) -> dict:

        logger.info("Roadmap Generation Started")

        result = generate_learning_roadmap(
            pdf_path,
            role
        )

        logger.info("Roadmap Generation Completed")

        return result