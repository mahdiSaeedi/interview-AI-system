from pydantic import BaseModel


class InterviewQuestion(BaseModel):
    id: str
    prompt: str


class AnswerItem(BaseModel):
    question_id: str
    response: str


class StartInterviewRequest(BaseModel):
    interview_title: str
    questions: list[InterviewQuestion]


class InterviewSession(BaseModel):
    session_id: str
    interview_title: str
    questions: list[InterviewQuestion]
    answers: list[AnswerItem]
    current_question_index: int
    is_complete: bool


class AnswerSubmission(BaseModel):
    session_id: str
    question_id: str
    response: str
