from agents.agent_base import AgentBase
from agents.agent_states import AgentState

class ManagerAgent(AgentBase):
    def __init__(self, llm):
        self.name = "ManagerAgent"
        super().__init__(llm)

    async def run(self, state: AgentState) -> AgentState:
        # Implement the logic for the manager agent here
        pass
