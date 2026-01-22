from urllib import response
import config
from agents.agent_base import AgentBase
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from states.state1 import AgentState


class ToolSolverAgent(AgentBase):
    def __init__(self, llm, llm_with_tools):
        super().__init__(llm)
        self.llm_with_tools = llm_with_tools

    # Nodes return a “state update”, not a new state object
    async def __call__(self, state: AgentState) -> dict:  # __call__ method lets a class instance be called as a function, LangGraph expects nodes to be callables
        messages = state.get("messages", [])
        
        # Scenario 2 (1 in the code below): tool already ran - getting final answer
        tool_messages = [m for m in messages if isinstance(m, ToolMessage)]  # empty if no tool call yet (like in the first pass)
        if tool_messages:
            system_prompt = SystemMessage(
                content=(
                    "You previously called a tool to solve the Color Blocks problem.\n"
                    "Using the tool result, output the final answer in the format(So show the solution and the reasoning behind it, you used the A* search algorithm):\n"
                    "COST: <integer>\n"
                    "REASON: <short explanation>"
                )
            )

            # response = await self.llm.ainvoke([system_prompt] + messages)
            response = await self.llm.ainvoke([system_prompt] + messages)   # Use a plain LLM here to avoid re-invoking tools

            # return {"messages": messages + [response]}   # Return the full response object to preserve tool call details, not just the text content.
            return {
                "messages": messages + [response],
                config.tools_usage_solver_output_field: response.content
            }

        


        # Scenario 1: no tool call yet - first pass

        system_prompt = SystemMessage(
            content=(
                "You are an AI agent that MUST use the provided tool that solves the Color Blocks problem.\n"
                "'color_blocks_astar_cost' to compute the solution cost.\n"
                "Call the tool exactly once.\n"
                "Then show the solution and explain briefly how the cost was obtained(you used the A* search algorithm)."
            )
        )

        user_prompt = HumanMessage(
            content=(
                f"Color Blocks problem:\n"
                f"Start blocks: {state[config.state_start_blocks_field]}\n"
                f"Goal fronts: {state[config.state_goal_blocks_field]}\n\n"
                "Use the tool and then output in the following format(So show the solution and the reasoning behind it, you used the A* search algorithm):\n"
                "COST: <integer>\n"
                "REASON: <short explanation>"
            )
        )
        
        response = await self.llm_with_tools.ainvoke([system_prompt, user_prompt])
        # response is an AIMessage
        # return a dictionary describing what he added or updated.
        
        # return {config.self_solver_output_field: response.content}  #! cannot do this here because then the tool call result is not visible to tools_condition and the ToolNode

        # CRITICAL: tools_condition only inspects `messages`, here, after this agent call, we must add the response to state["messages"] so that the tool call result is visible to tools_condition and the ToolNode
        return {"messages": messages + [response]}  # Append the new response to existing messages


