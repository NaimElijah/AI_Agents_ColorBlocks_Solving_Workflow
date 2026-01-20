from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from tools.color_blocks_tool import color_blocks_astar_cost
from states.state1 import AgentState
from agents.self_solver_agent import SelfSolverAgent
from agents.tool_solver_agent import ToolSolverAgent
from agents.manager_agent import ManagerAgent

# 2 options of using tools here: either bind the tools to the LLM before passing it to the agent, or use a ToolNode in the graph. We'll use a ToolNode here.
# General Note: Agents transform state; graphs control execution.

# def build_graph(llm, llm_with_tools):   # with binding tools to LLM
def build_graph(llm):                 # without binding tools to LLM, we use a ToolNode instead

    graph = StateGraph(AgentState)
    
    # Define nodes
    graph.add_node("manager", ManagerAgent(llm))
    graph.add_node("self_solver", SelfSolverAgent(llm))
    # graph.add_node("with_tools_solver", ToolSolverAgent(llm_with_tools))
    graph.add_node("with_tools_solver", ToolSolverAgent(llm))
    
    graph.add_node("tools", ToolNode([color_blocks_astar_cost]))   # Tool node to use the color blocks cost tool

    # Define edges
    graph.add_edge(START, "manager")                 # Start --> manager agent

    graph.add_edge("manager", "self_solver")         # manager agent --> self-solving agent
    graph.add_edge("manager", "with_tools_solver")   # manager agent --> with-tools solver agent

    graph.add_edge("self_solver", "manager")         # self-solving agent --> manager agent
    
    # Note: here I don't want a loop back from tools to with_tools_solver, I want the with-tools solver to only call the tools once per request
    graph.add_edge("with_tools_solver", "tools")     # with-tools solver agent --> tools
    graph.add_edge("tools", "manager")               # tools --> manager agent

    graph.add_edge("manager", END)                   # manager agent --> End

    return graph.compile()                           # Compile the graph for execution
