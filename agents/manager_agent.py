from agents.agent_base import AgentBase
from langchain_core.messages import SystemMessage, HumanMessage
from states.state1 import AgentState


class ManagerAgent(AgentBase):
    def __init__(self, llm):
        super().__init__(llm)

    async def __call__(self, state: AgentState) -> dict:
        self_res = state.get("SelfSolverAgent_output")   # Get outputs from previous agents, who were called before in the graph and added to the state
        tool_res = state.get("ToolSolverAgent_output")   # Get outputs from previous agents, who were called before in the graph and added to the state

        system_prompt = SystemMessage(
            content=(
                "You are a manager agent acting as an LLM-as-a-judge.\n"
                "Compare two solutions to the same color blocks problem.\n"
                "Explain differences and give a short summary.\n"
                "Prefer reliable, algorithmic solutions when appropriate."
            )
        )

        user_prompt = HumanMessage(
            content=(
                "Color Blocks solution comparison:\n\n"
                f"Self-solver output:\n{self_res}\n\n"
                f"Tool-based solver output:\n{tool_res}\n\n"
                "Output in the following format:\n"
                "DIFFERENCES: <list differences>\n"
                "SUMMARY: <2-4 sentences>\n"
                "FINAL_DECISION: <which solution is more reliable and why>"
            )
        )

        response = await self.llm.ainvoke([system_prompt, user_prompt])
        # return a dictionary describing what he added or updated.
        return {"manager_feedback": response.content}

