from mcp.server.fastmcp import FastMCP
from Heuristic_color_blocks_search_code.heuristics import base_heuristic, init_goal_for_heuristics, advanced_heuristic
from Heuristic_color_blocks_search_code.color_blocks_state import color_blocks_state, init_goal_for_search
from heuristic_search import search

# Initialize FastMCP, with a custom name for the tool set.
mcp = FastMCP("Color Blocks Tools")

@mcp.tool()
def color_blocks_astar_cost(start_blocks: str, goal_blocks: str, heuristic="base") -> int:
    """Uses A* search algorithm function to find the cost of the optimal solution from start_blocks to goal_blocks using the specified heuristic."""
    init_goal_for_heuristics(goal_blocks)
    init_goal_for_search(goal_blocks)
    start_state = color_blocks_state(start_blocks)
    if heuristic == "advanced":
        return search(start_state, advanced_heuristic)[-1].g      # need to return the cost only
    return search(start_state, base_heuristic)[-1].g              # need to return the cost only

    # return solve_color_blocks_cost(start_blocks, goal_blocks, heuristic)

