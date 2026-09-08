from pydantic import BaseModel
from typing import List


class LearningModule(BaseModel):

    title: str

    topics: List[str]

    resources: List[str]


class RoadmapReport(BaseModel):

    roadmap: List[LearningModule]