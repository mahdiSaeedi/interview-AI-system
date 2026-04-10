from app.schemas.interview import InterviewSession


class SessionStore:
    def __init__(self) -> None:
        self._sessions: dict[str, InterviewSession] = {}

    def save(self, session: InterviewSession) -> None:
        self._sessions[session.session_id] = session

    def get(self, session_id: str) -> InterviewSession | None:
        return self._sessions.get(session_id)


session_store = SessionStore()
