from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from tools.color_blocks_tool import color_blocks_astar_cost
from agents.agent_states import AgentState
from agents.self_solver_agent import self_solver_agent
from agents.my_solver_agent import my_solver_agent
from agents.manager_agent import manager_agent


def build_graph(llm, llm_with_tools):
    # graph = StateGraph(AgentState)    #TODO: see what to use here
    graph = StateGraph(MessagesState)
    
    # Define nodes
    graph.add_node("manager", manager_agent(llm))
    graph.add_node("self_solver", self_solver_agent(llm))
    graph.add_node("with_tools_solver", my_solver_agent(llm_with_tools))
    graph.add_node("tools", ToolNode([color_blocks_astar_cost]))

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
