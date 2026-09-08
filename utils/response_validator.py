from pydantic import ValidationError

from config.logging_config import setup_logger

from models.ats_schema import ATSReport
from models.jd_schema import JDMatchReport
from models.interview_schema import InterviewReport
from models.roadmap_schema import RoadmapReport

logger = setup_logger()


def validate_ats_response(data: dict) -> dict:

    try:

        report = ATSReport(**data)

        return report.model_dump()

    except ValidationError as error:

        logger.exception(error)

        raise ValueError(
            "Invalid ATS Response"
        )


def validate_jd_response(data: dict) -> dict:

    try:

        report = JDMatchReport(**data)

        return report.model_dump()

    except ValidationError as error:

        logger.exception(error)

        raise ValueError(
            "Invalid JD Response"
        )

def validate_interview_response(data: dict) -> dict:

    report = InterviewReport(**data)

    return report.model_dump()

def validate_roadmap_response(data: dict):

    report = RoadmapReport(**data)

    return report.model_dump()