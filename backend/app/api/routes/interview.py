from fastapi import APIRouter, HTTPException

from app.agents.interview_conductor import InterviewConductorAgent
from app.schemas.interview import AnswerSubmission, InterviewSession, StartInterviewRequest
from app.services.session_store import session_store


router = APIRouter()
agent = InterviewConductorAgent(store=session_store)


@router.post("/start", response_model=InterviewSession)
def start_interview(payload: StartInterviewRequest) -> InterviewSession:
    return agent.start_session(payload)


@router.post("/answer", response_model=InterviewSession)
def submit_answer(payload: AnswerSubmission) -> InterviewSession:
    session = agent.submit_answer(payload)
    if session is None:
        raise HTTPException(status_code=404, detail="Interview session not found")
    return session
