from app.agents.base import AgentMetadata, BaseAgent
from app.schemas.instructions import InstructionRequest, QuestionItem, QuestionSetResponse


class QuestionGenerationAgent(BaseAgent):
    metadata = AgentMetadata(
        name="QuestionGenerationAgent",
        phase="question_generation",
    )

    def generate_questions(self, payload: InstructionRequest) -> QuestionSetResponse:
        questions = [
            QuestionItem(
                id=f"q-{index + 1}",
                prompt=f"Placeholder question {index + 1} for: {payload.title}",
                intent="Replace with instruction-aware generation logic.",
            )
            for index in range(3)
        ]
        return QuestionSetResponse(
            title=payload.title,
            questions=questions,
        )
