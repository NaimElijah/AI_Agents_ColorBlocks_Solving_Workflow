import config
from agents.agent_base import AgentBase
from states.state1 import AgentState
from langchain_core.messages import SystemMessage, HumanMessage


class SelfSolverAgent(AgentBase):
    def __init__(self, llm):
        super().__init__(llm)

     # Nodes return a “state update”, not a new state object
    async def __call__(self, state: AgentState) -> dict:   # __call__ method lets a class instance be called as a function, LangGraph expects nodes to be callables
        system_prompt = SystemMessage(
            content=(
                "You are an AI agent solving a heuristic search problem.\n"
                "You are NOT allowed to use any tools or external code.\n"
                "Try to reason about the solution cost.\n"
                "Return an integer cost and a short explanation."
            )
        )

        user_prompt = HumanMessage(
            content=(
                f"Color Blocks problem:\n"
                f"Start blocks: {state[config.state_start_blocks_field]}\n"
                f"Goal fronts: {state[config.state_goal_blocks_field]}\n\n"
                "Output in the following format:\n"
                "COST: <integer>\n"
                "REASON: <short explanation>"
            )
        )

        response = await self.llm.ainvoke([system_prompt, user_prompt])
        # return a dictionary describing what he added or updated.
        return {config.self_solver_output_field: response.content}
