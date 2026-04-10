from app.agents.base import AgentMetadata, BaseAgent
from app.schemas.analysis import AnalysisResponse
from app.services.session_store import SessionStore


class AnswerAnalysisAgent(BaseAgent):
    metadata = AgentMetadata(
        name="AnswerAnalysisAgent",
        phase="answer_analysis",
    )

    def __init__(self, store: SessionStore) -> None:
        self.store = store

    def analyze_session(self, session_id: str) -> AnalysisResponse | None:
        session = self.store.get(session_id)
        if session is None:
            return None

        answer_count = len(session.answers)
        summary = (
            "This is a placeholder qualitative analysis. "
            "Replace it with LLM-backed synthesis, themes, and recommendations."
        )
        themes = [
            "Initial structure created",
            f"Collected {answer_count} answer(s)",
            "Ready for richer analysis logic",
        ]
        return AnalysisResponse(
            session_id=session.session_id,
            summary=summary,
            themes=themes,
            recommendations=[
                "Add domain-specific analysis prompts.",
                "Store transcripts in persistent storage.",
                "Track confidence and missing-information signals.",
            ],
        )
