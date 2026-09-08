from pydantic import BaseModel
from typing import List


class InterviewQuestion(BaseModel):

    question: str

    answer: str

    difficulty: str


class InterviewReport(BaseModel):

    technical_questions: List[InterviewQuestion]

    hr_questions: List[InterviewQuestion]

    project_questions: List[InterviewQuestion]

    scenario_questions: List[InterviewQuestion]