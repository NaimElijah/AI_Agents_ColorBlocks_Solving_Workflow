from urllib import response
import config
from agents.agent_base import AgentBase
from langchain_core.messages import SystemMessage, HumanMessage
from states.state1 import AgentState
from tools.color_blocks_tool import color_blocks_astar_cost


class ToolSolverAgent(AgentBase):
    def __init__(self, llm):
        super().__init__(llm)

    async def __call__(self, state: AgentState) -> AgentState:  # __call__ method lets a class instance be called as a function, LangGraph expects nodes to be callables
        system_prompt = SystemMessage(
            content=(
                "You are an AI agent that MUST use the provided tool"
                "'color_blocks_astar_cost' to compute the solution cost.\n"
                "Call the tool exactly once.\n"
                "Then explain briefly how the cost was obtained."
            )
        )

        user_prompt = HumanMessage(
            content=(
                f"Color Blocks problem:\n"
                f"Start blocks: {state[config.state_start_blocks_field]}\n"
                f"Goal fronts: {state[config.state_goal_blocks_field]}\n\n"
                "Use the tool and then output in the following format:\n"
                "COST: <integer>\n"
                "REASON: <short explanation>"
            )
        )

        response = await self.llm.ainvoke([system_prompt, user_prompt])
        # return a dictionary describing what he added or updated.
        # #? DEBUG
        # print("--> DEBUG tool solver response:", response)
        # print("--> DEBUG tool calls (response.tool_calls):", response.tool_calls)
        # print("--> DEBUG tool messages (response.tool_messages):", response.tool_messages)
        # print("--> DEBUG tool response.content:", response.content)
        # #? DEBUG
        # return {config.tools_usage_solver_output_field: response.content}
        return {config.tools_usage_solver_output_field: [response]}           # Return the full response object to preserve tool call details, not just the text content.
        # return {"messages": [response]}                                     # Return the full response object to preserve tool call details, not just the text content.

    