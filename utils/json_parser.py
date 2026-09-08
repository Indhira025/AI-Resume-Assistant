"""
JSON Parser Utility

This module cleans, parses and validates
AI responses returned by Ollama.

Supports

1. ATS
2. JD Matching
3. Interview Questions

Author : AI Resume Optimizer
"""

import json
import re

from config.logging_config import setup_logger

from utils.response_validator import (
    validate_ats_response,
    validate_jd_response,
    validate_interview_response,
    validate_roadmap_response
)
logger = setup_logger()


def clean_json(text: str) -> str:
    """
    Clean common LLM formatting issues.
    """

    if not text:
        return ""

    # Remove markdown fences
    text = text.replace("```json", "")
    text = text.replace("```", "")

    text = text.strip()

    # Remove headings produced by LLM
    text = re.sub(
        r"Here are.*?:",
        "",
        text,
        flags=re.IGNORECASE | re.DOTALL
    )

    text = re.sub(
        r"Technical Questions\s*:",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"HR Questions\s*:",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"Project Questions\s*:",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"Scenario Questions\s*:",
        "",
        text,
        flags=re.IGNORECASE
    )

    return text.strip()


def parse_json(
    ai_response: str,
    response_type: str = "ats"
):
    """
    Parse AI response.
    """

    cleaned = clean_json(ai_response)

    logger.info("AI response cleaned.")

    try:

        # ---------------- Interview ----------------

        if response_type == "interview":

            start = cleaned.find("{")
            end = cleaned.rfind("}")

            if start == -1 or end == -1:
                raise ValueError("Interview JSON not found.")

            cleaned = cleaned[start:end + 1]

            data = json.loads(cleaned)

            logger.info("Interview JSON parsed successfully.")

            return validate_interview_response(data)


        # ---------- ATS / JD ----------

        start = cleaned.find("{")
        end = cleaned.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("No JSON found.")

        cleaned = cleaned[start:end + 1]

        data = json.loads(cleaned)

        logger.info("JSON parsed successfully.")

        if response_type == "ats":
            return validate_ats_response(data)

        if response_type == "roadmap":
            return validate_roadmap_response(data)

        elif response_type == "jd":
            return validate_jd_response(data)

        return data

    except Exception as error:

        logger.exception(error)

        logger.error(ai_response)

        raise ValueError(
            "AI returned invalid JSON."
        )