import config
from agents.agent_base import AgentBase
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from states.state1 import AgentState


class ManagerAgent(AgentBase):
    def __init__(self, llm):
        super().__init__(llm)

    async def __call__(self, state: AgentState) -> dict:
        self_res = state.get(config.self_solver_output_field)          # Get outputs from previous agents, who were called before in the graph and added to the state
        tool_user_res = state.get(config.tools_usage_solver_output_field)
        # he doesn't get a message from the tool-using agent directly, but from the tool node that was called after it, we get that here later below

        tool_result = None
        for msg in state.get(config.tools_usage_solver_output_field, []):
            if isinstance(msg, ToolMessage):
                tool_result = msg.content   # Get outputs from previous tool used, who were called before in the graph and added to the state

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
                f"Tool-based solver output:\n{tool_user_res}\n\n"
                "Output in the following format:\n"
                "DIFFERENCES: <list differences>\n"
                "SUMMARY: <2-4 sentences>\n"
                "FINAL_DECISION: <which solution is more reliable and why>"
            )
        )

        response = await self.llm.ainvoke([system_prompt, user_prompt])
        # return a dictionary describing what he added or updated.
        return {config.manager_feedback_field: response.content}

