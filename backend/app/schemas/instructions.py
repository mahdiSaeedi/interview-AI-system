from pydantic import BaseModel, Field


class InstructionRequest(BaseModel):
    title: str = Field(..., description="Interview title")
    instructions: str = Field(..., description="Instructions used to generate questions")


class QuestionItem(BaseModel):
    id: str
    prompt: str
    intent: str | None = None


class QuestionSetResponse(BaseModel):
    title: str
    questions: list[QuestionItem]
