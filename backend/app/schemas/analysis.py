from pydantic import BaseModel


class AnalysisResponse(BaseModel):
    session_id: str
    summary: str
    themes: list[str]
    recommendations: list[str]
