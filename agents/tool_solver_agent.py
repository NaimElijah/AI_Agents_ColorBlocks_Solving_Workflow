from agents.agent_base import AgentBase
from types.state import AgentState
from tools.color_blocks_tool import color_blocks_astar_cost

class ToolSolverAgent(AgentBase):
    def __init__(self, llm):
        super().__init__(llm)

    async def __call__(self, state: AgentState) -> AgentState: # __call__ method lets a class instance be called as a function, LangGraph expects nodes to be callables
        # return a dictionary describing what he added or updated.
        return {"ToolSolverAgent_output": color_blocks_astar_cost(state["start_blocks"], state["goal_blocks"])}
    
    
