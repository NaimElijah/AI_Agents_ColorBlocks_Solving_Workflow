import asyncio
import config
from graph.agent_graph import build_graph
from llm.llm_factory import get_llm, get_llm_with_tools
from tools.color_blocks_tool import color_blocks_astar_cost

# 2 options of using tools here: either bind the tools to the LLM before passing it to the agent, or use a ToolNode in the graph. We'll use tool binding here.
# General Note: Agents transform state; graphs control execution.
# An async main function to run the graph
async def main():

    llm = get_llm()

    graph = build_graph(llm)        # Build the graph & compile it

    # The problems in a "start_blocks|goal_blocks" format
    problems = [
        # Example 1
        "(5,2),(1,3),(9,22),(21,4)|2,22,4,3",
        # Example 2
        "(5,2),(1,3),(9,22),(21,4)|2,1,9,21",
        # Example 3
        "(5,2),(1,3),(9,22),(21,4),(11,12),(12,13),(13,14)|11,2,1,14,9,13,21"
    ]
    
    print(f"Starting Agentic Workflow for {len(problems)} Color Blocks Problems...\n\n")
    
    for i, problem in enumerate(problems, 1):
        start_blocks, goal_blocks = problem.split("|")

        print(f"--- Processing Problem {i} ---\n")
        print(f"Input:\nStart Blocks: {start_blocks}\nGoal Blocks: {goal_blocks}\n")
        
        try:
            # Prepare the initial state, LangGraph adds to it later as needed from agents responses/returns
            initial_state = {
                config.state_start_blocks_field: start_blocks,
                config.state_goal_blocks_field: goal_blocks,
                "messages": []
            }

             # Invoke the graph with an initial state, awaitably, it means we can use async agents inside
            result = await graph.ainvoke(initial_state)
            # the graph returns a dictionary with all the outputs from the nodes, which is the final state of the graph
            
            print("-" * 40 + "\n")
            print(f"\nToolSolverAgent_output: {result.get(config.tools_usage_solver_output_field)}\n")
            print("-" * 40 + "\n")
            print(f"\nSelfSolverAgent_output: {result.get(config.self_solver_output_field)}\n")
            print("-" * 40 + "\n")
            print(f"\nManagerAgent_feedback: {result.get(config.manager_feedback_field)}\n")
            print("-" * 40 + "\n")

        except Exception as e:
            print(f"Error processing problem {i}: {e.__str__()}\n")




if __name__ == "__main__":
    asyncio.run(main())