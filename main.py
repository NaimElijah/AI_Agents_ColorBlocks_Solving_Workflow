import sys
import os

from graph.agent_graph import build_graph

# # Ensure project root is in path for module imports
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# from src.graph import create_workflow_graph

async def main():
    graph = build_graph(...)
    result = await graph.ainvoke({
        "start_blocks": "...",
        "goal_blocks": "...",
        "heuristic": "base"
    })

    print(result)








    # graph = create_workflow_graph()
    
    # # Define problems based on simple_test.py
    # # Format: Start: <start> Goal: <goal>
    # problems = [
    #     # Example 1
    #     "Start: (5,2),(1,3),(9,22),(21,4) Goal: 2,22,4,3",
    #     # Example 2
    #     "Start: (5,2),(1,3),(9,22),(21,4) Goal: 2,1,9,21",
    #     # Example 3
    #     "Start: (5,2),(1,3),(9,22),(21,4),(11,12),(12,13),(13,14) Goal: 11,2,1,14,9,13,21"
    # ]
    
    # print("Starting Agentic Workflow for Color Blocks Problems...\n")
    
    # for i, problem in enumerate(problems, 1):
    #     print(f"--- Processing Problem {i} ---")
    #     print(f"Input: {problem}")
        
    #     try:
    #         initial_state = {"input_problem": problem}
    #         result = graph.invoke(initial_state)
            
    #         print("\n[My Solver Output]:")
    #         print(result.get("my_solver_output"))
            
    #         print("\n[Self Solver Output]:")
    #         print(result.get("self_solver_output"))
            
    #         print("\n[Manager Comparison]:")
    #         print(result.get("comparison_result"))
    #         print("-" * 50 + "\n")
            
    #     except Exception as e:
    #         print(f"Error processing problem {i}: {e}\n")

if __name__ == "__main__":
    main()
