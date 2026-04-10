from dataclasses import dataclass


@dataclass(slots=True)
class AgentMetadata:
    name: str
    phase: str


class BaseAgent:
    metadata: AgentMetadata

    def describe(self) -> dict[str, str]:
        return {
            "name": self.metadata.name,
            "phase": self.metadata.phase,
        }
