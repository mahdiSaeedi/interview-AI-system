import uuid

from app.agents.base import AgentMetadata, BaseAgent
from app.schemas.interview import (
    AnswerItem,
    AnswerSubmission,
    InterviewQuestion,
    InterviewSession,
    StartInterviewRequest,
)
from app.services.session_store import SessionStore


class InterviewConductorAgent(BaseAgent):
    metadata = AgentMetadata(
        name="InterviewConductorAgent",
        phase="interview_conduction",
    )

    def __init__(self, store: SessionStore) -> None:
        self.store = store

    def start_session(self, payload: StartInterviewRequest) -> InterviewSession:
        session = InterviewSession(
            session_id=str(uuid.uuid4()),
            interview_title=payload.interview_title,
            questions=[
                InterviewQuestion(id=question.id, prompt=question.prompt)
                for question in payload.questions
            ],
            answers=[],
            current_question_index=0,
            is_complete=False,
        )
        self.store.save(session)
        return session

    def submit_answer(self, payload: AnswerSubmission) -> InterviewSession | None:
        session = self.store.get(payload.session_id)
        if session is None or session.is_complete:
            return session

        session.answers.append(
            AnswerItem(
                question_id=payload.question_id,
                response=payload.response,
            )
        )

        next_index = session.current_question_index + 1
        session.current_question_index = next_index
        session.is_complete = next_index >= len(session.questions)
        self.store.save(session)
        return session
