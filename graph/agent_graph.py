from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from tools.color_blocks_tool import color_blocks_astar_cost
from states.state1 import AgentState
from agents.self_solver_agent import SelfSolverAgent
from agents.tool_solver_agent import ToolSolverAgent
from agents.manager_agent import ManagerAgent
from llm.llm_factory import get_llm_with_tools

# 2 options of using tools here: either bind the tools to the LLM before passing it to the agent, or use a ToolNode in the graph. We'll use tool binding here.
# General Note: Agents transform state; graphs control execution.
# Nodes return a “state update”, not a new state object

#* Another graph with conditional tool execution   <<---------------
def build_graph(llm):
    tools = [color_blocks_astar_cost]
    llm_with_tools = get_llm_with_tools(tools)

    graph = StateGraph(AgentState)

    # Nodes
    graph.add_node("self_solver", SelfSolverAgent(llm))
    graph.add_node("with_tools_solver", ToolSolverAgent(llm_with_tools))
    graph.add_node("tools", ToolNode(tools))
    graph.add_node("manager", ManagerAgent(llm))

    # START fan-out
    graph.add_edge(START, "self_solver")
    graph.add_edge(START, "with_tools_solver")

    # Self solver goes directly to manager
    graph.add_edge("self_solver", "manager")

    # Tool solver → conditional tool execution
    # When you use tools_condition, you are in MessagesState / chat-agent mode, even if you have a custom AgentState
    # Tool execution happens ONLY through messages. Tool results arrive as ToolMessage objects inside messages
    graph.add_conditional_edges("with_tools_solver", tools_condition,
        # {
        #     "tools": "tools",
        #     END: "manager",   # when no tool call → go to manager
        # }
    )   # may work with ot without the last arg(the {...})

    # Tool execution → back to solver
    graph.add_edge("tools", "with_tools_solver")

    # Manager → END
    graph.add_edge("manager", END)

    return graph.compile()


# flow: START → self_solver & with_tools_solver → manager → END
# def build_graph(llm, llm_with_tools):
# def build_graph(llm):
#     a_star_tools = [color_blocks_astar_cost]
#     llm_with_tools = get_llm_with_tools(a_star_tools)

#     graph = StateGraph(AgentState)

#     # Define nodes
#     graph.add_node("self_solver", SelfSolverAgent(llm))
#     graph.add_node("with_tools_solver", ToolSolverAgent(llm_with_tools))
#     # graph.add_node("with_tools_solver", ToolSolverAgent(llm))
#     graph.add_node("manager", ManagerAgent(llm))

#     graph.add_node("tools", ToolNode(a_star_tools))  # Tool node to use the color blocks cost tool

#     # Define edges
#     graph.add_edge(START, "self_solver")
#     graph.add_edge(START, "with_tools_solver")

#     graph.add_edge("self_solver", "manager")
#     # graph.add_edge("with_tools_solver", "manager")

#     graph.add_edge("with_tools_solver", "tools")     # with-tools solver agent --> tools
#     graph.add_edge("tools", "manager")               # tools --> manager agent

#     graph.add_edge("manager", END)

#     return graph.compile()



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



