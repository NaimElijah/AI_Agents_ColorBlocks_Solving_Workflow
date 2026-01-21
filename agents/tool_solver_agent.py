from urllib import response
import config
from agents.agent_base import AgentBase
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from states.state1 import AgentState


class ToolSolverAgent(AgentBase):
    def __init__(self, llm):
        super().__init__(llm)

    # Nodes return a “state update”, not a new state object
    async def __call__(self, state: AgentState) -> dict:  # __call__ method lets a class instance be called as a function, LangGraph expects nodes to be callables
        messages = state.get("messages", [])
        
        # 🔁 SECOND(II) PASS: tool already ran
        tool_messages = [m for m in messages if isinstance(m, ToolMessage)]  # empty if no tool call yet (like in the first pass)
        if tool_messages:
            system_prompt = SystemMessage(
                content=(
                    "You previously called a tool to solve the Color Blocks problem.\n"
                    "Using the tool result, output the final answer in the format:\n"
                    "COST: <integer>\n"
                    "REASON: <short explanation>"
                )
            )

            response = await self.llm.ainvoke([system_prompt] + messages)
            
            # #? DEBUG
            print("--> AFTER DEBUG --> tool solver response:", response)
            print("--> AFTER DEBUG --> tool calls (response.tool_calls):", response.tool_calls)
            print("--> AFTER DEBUG --> tool response.content:", response.content)
            # #? DEBUG

            return {"messages": messages + [response]}   # Return the full response object to preserve tool call details, not just the text content.
        


        # 🔁 FIRST(I) PASS: no tool call yet (gets here if no tool call yet)

        system_prompt = SystemMessage(
            content=(
                "You are an AI agent that MUST use the provided tool that solves the Color Blocks problem.\n"
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
        # response is an AIMessage
        # return a dictionary describing what he added or updated.
        # #? DEBUG
        print("--> BEFORE DEBUG --> tool solver response:", response)
        print("--> BEFORE DEBUG --> tool calls (response.tool_calls):", response.tool_calls)
        print("--> BEFORE DEBUG --> tool response.content:", response.content)
        # #? DEBUG
        # return {config.tools_usage_solver_output_field: response.content}
        # return {config.tools_usage_solver_output_field: [response]}           # Return the full response object to preserve tool call details, not just the text content.
        
        # CRITICAL: tools_condition only inspects `messages`, here, after this agent call, we must add the response to state["messages"] so that the tool call result is visible to tools_condition and the ToolNode
        return {"messages": messages + [response]}  # Append the new response to existing messages

        # return {"messages": [response]}                                     # Return the full response object to preserve tool call details, not just the text content.

    