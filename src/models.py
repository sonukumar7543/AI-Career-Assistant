from pydantic import BaseModel
from typing import List, Dict


class Recommendation(BaseModel):
    difficulty: str
    resource: str


class AnalysisResponse(BaseModel):
    candidate: str
    score: float
    matched_skills: List[str]
    missing_skills: List[str]
    recommendations: Dict[str, Recommendation]