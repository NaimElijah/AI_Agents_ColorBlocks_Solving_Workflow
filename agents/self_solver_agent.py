from agents.agent_base import AgentBase
from agents.agent_states import AgentState

class SelfSolverAgent(AgentBase):
    def __init__(self, llm):
        self.name = "SelfSolverAgent"
        super().__init__(llm)

    async def __call__(self, state: AgentState) -> AgentState: # __call__ method lets a class instance be called as a function, LangGraph expects nodes to be callables
        # Implement the logic for the self-solving agent here
        pass
    

