from fastapi import APIRouter, HTTPException

from app.agents.answer_analysis import AnswerAnalysisAgent
from app.schemas.analysis import AnalysisResponse
from app.services.session_store import session_store


router = APIRouter()
agent = AnswerAnalysisAgent(store=session_store)


@router.get("/session/{session_id}", response_model=AnalysisResponse)
def analyze_session(session_id: str) -> AnalysisResponse:
    analysis = agent.analyze_session(session_id)
    if analysis is None:
        raise HTTPException(status_code=404, detail="Interview session not found")
    return analysis
