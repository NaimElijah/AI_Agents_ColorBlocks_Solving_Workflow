from agents.agent_base import AgentBase
from types.state import AgentState

class ManagerAgent(AgentBase):
    def __init__(self, llm, selfAgent, toolAgent):
        self.name = "ManagerAgent"
        super().__init__(llm)
        self.selfAgent = selfAgent
        self.toolAgent = toolAgent

    async def run(self, state: AgentState) -> AgentState:
        # Implement the logic for the manager agent here
        self_res = state["SelfSolverAgent_output"]
        my_res = state["ToolSolverAgent_output"]

        # run the other 2 agents and compare their results
        self_res = await self.selfAgent(state)
        my_res = await self.toolAgent(state)

        prompt = f"compare the results of the two agents:\nSelf Solver Result: {self_res}\nTool Solver Result: {my_res}\nProvide feedback on their performance."
        manager_feedback = await self.llm.apredict(prompt)

        #TODO: with llm, compare the results properly

        # return a dictionary describing what he added or updated.
        return {"manager_feedback": manager_feedback}

