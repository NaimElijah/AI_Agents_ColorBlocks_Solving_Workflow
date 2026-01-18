import time
from heuristics import *
from heuristic_search import *
from search import *

if __name__ == '__main__':
    # * Example .1. *
    # start_blocks = "(5,2),(1,3),(9,22),(21,4)"
    # goal_blocks = "2,22,4,3"
    # * Example .2. *
    # start_blocks = "(5,2),(1,3),(9,22),(21,4)"
    # goal_blocks = "2,1,9,21"
    # * Example .3. *
    start_blocks = "(5,2),(1,3),(9,22),(21,4),(11,12),(12,13),(13,14)"
    goal_blocks = "11,2,1,14,9,13,21"

    init_goal_for_heuristics(goal_blocks)
    init_goal_for_search(goal_blocks)
    start_state = color_blocks_state(start_blocks)

    start_time = time.time()
    search_result = search(start_state, base_heuristic)    # the heuristic search being executed.
    end_time = time.time() - start_time

    # runtime
    print(end_time)
    # solution cost
    print(search_result[-1].g)