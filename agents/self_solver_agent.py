from agents.agent_base import AgentBase
from types.state import AgentState

class SelfSolverAgent(AgentBase):
    def __init__(self, llm):
        super().__init__(llm)

    async def __call__(self, state: AgentState) -> AgentState: # __call__ method lets a class instance be called as a function, LangGraph expects nodes to be callables
        # TODO: Implement the logic for the self-solving agent here
        # the self solver just gives the LLM the problem to solve without tools
        # prompt = f"Solve the problem with start blocks: {state['start_blocks']} and goal blocks: {state['goal_blocks']} without using any tools."
        # response = await self.llm.apredict(prompt)

        # return a dictionary describing what he added or updated.
        return {"SelfSolverAgent_output": "--->>  SELF SOLVER RESULT HERE  <<---"}
    

