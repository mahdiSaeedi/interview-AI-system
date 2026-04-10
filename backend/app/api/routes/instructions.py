from fastapi import APIRouter

from app.agents.question_generation import QuestionGenerationAgent
from app.schemas.instructions import InstructionRequest, QuestionSetResponse


router = APIRouter()
agent = QuestionGenerationAgent()


@router.post("/generate-questions", response_model=QuestionSetResponse)
def generate_questions(payload: InstructionRequest) -> QuestionSetResponse:
    return agent.generate_questions(payload)
