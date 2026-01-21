from typing import TypedDict, List
from langchain_core.messages import BaseMessage

# Define the state structure for the agents, using TypedDict for type safety, flexibility, and clarity, with optional fields, no logic should be here.
class AgentState(TypedDict, total=False):  # total=False makes all fields optional
    start_blocks: str
    goal_blocks: str
    messages: List[BaseMessage]   # required to store the conversation messages, including tool calls and responses, for tools-using agents
    SelfSolverAgent_output: str
    ToolSolverAgent_output: str
    manager_feedback: str
    # Add other state fields as needed
    #! These field names need to match the state field names in the config.py
