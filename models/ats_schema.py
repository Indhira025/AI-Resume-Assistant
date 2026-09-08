from pydantic import BaseModel
from typing import List


class ATSReport(BaseModel):

    ats_score: int

    strengths: List[str]

    weaknesses: List[str]

    missing_skills: List[str]

    grammar_issues: List[str]

    recommendations: List[str]