from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from tools.color_blocks_tool import color_blocks_astar_cost
from states.state1 import AgentState
from agents.self_solver_agent import SelfSolverAgent
from agents.tool_solver_agent import ToolSolverAgent
from agents.manager_agent import ManagerAgent
from llm.llm_factory import get_llm_with_tools

# 2 options of using tools here: either bind the tools to the LLM before passing it to the agent, or use a ToolNode in the graph. We'll use tool binding here.
# General Note: Agents transform state; graphs control execution.

# flow: START → self_solver & with_tools_solver → manager → END
def build_graph(llm):
    llm_with_tools = get_llm_with_tools([color_blocks_astar_cost])

    graph = StateGraph(AgentState)

    # Define nodes
    graph.add_node("self_solver", SelfSolverAgent(llm))
    graph.add_node("with_tools_solver", ToolSolverAgent(llm_with_tools))
    # graph.add_node("with_tools_solver", ToolSolverAgent(llm))
    graph.add_node("manager", ManagerAgent(llm))

    graph.add_node("tools", ToolNode([color_blocks_astar_cost]))  # Tool node to use the color blocks cost tool

    # Define edges
    graph.add_edge(START, "self_solver")
    graph.add_edge(START, "with_tools_solver")

    graph.add_edge("self_solver", "manager")
    # graph.add_edge("with_tools_solver", "manager")

    graph.add_edge("with_tools_solver", "tools")     # with-tools solver agent --> tools
    graph.add_edge("tools", "manager")               # tools --> manager agent

    graph.add_edge("manager", END)

    return graph.compile()



# if we want to avoid a cycle and put the manager first, then both solvers, then back to manager, we can do this: 
# add to class AgentState(TypedDict, total=False):
#            start_blocks: str
#            goal_blocks: str
#            phase: str
# and add conditional edges like this:
# if state["phase"] == "init":
#     manager → solvers
# elif state["phase"] == "judge":
#     manager → END


# flow: START → manager → self_solver & with_tools_solver → manager → END
# def build_graph(llm, llm_with_tools):
# def build_graph(llm):                     # without binding tools to LLM, we use a ToolNode instead
#     llm_with_tools = get_llm_with_tools([color_blocks_astar_cost])
    
#     graph = StateGraph(AgentState)
    
#     # Define nodes
#     graph.add_node("manager", ManagerAgent(llm))
#     graph.add_node("self_solver", SelfSolverAgent(llm))
#     graph.add_node("with_tools_solver", ToolSolverAgent(llm_with_tools))
#     # graph.add_node("with_tools_solver", ToolSolverAgent(llm))

#     graph.add_node("tools", ToolNode([color_blocks_astar_cost]))  # Tool node to use the color blocks cost tool, this is another way of using tools in the graph, instead of binding them to the LLM

#     # Define edges
#     graph.add_edge(START, "manager")                 # Start --> manager agent

#     graph.add_edge("manager", "self_solver")         # manager agent --> self-solving agent
#     graph.add_edge("manager", "with_tools_solver")   # manager agent --> with-tools solver agent

#     # Note: here I don't want a loop back from tools to with_tools_solver, I want the with-tools solver to only call the tools once per request
#     graph.add_edge("with_tools_solver", "tools")     # with-tools solver agent --> tools
#     graph.add_edge("tools", "manager")               # tools --> manager agent

#     graph.add_edge("self_solver", "manager")         # self-solving agent --> manager agent
#     # graph.add_edge("with_tools_solver", "manager")   # with-tools solver agent --> manager agent

#     graph.add_edge("manager", END)                   # manager agent --> End

#     return graph.compile()                           # Compile the graph for execution


