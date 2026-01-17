import re
from color_blocks_state import color_blocks_state

# you can add helper functions and params
goal_pairs = set()        # unordered adjacency pairs
goal_fronts = []          # list of ordered goal front values

# goal_blocks is a String representing the final goal state of the blocks.
def init_goal_for_heuristics(goal_blocks):
    global goal_pairs, goal_fronts
    goal_fronts = [int(x) for x in goal_blocks.split(",")]
    l, gp = len(goal_fronts), set()
    for i in range(l - 1):
        a = goal_fronts[i]
        b = goal_fronts[i + 1]
        if a <= b:
            gp.add((a, b))
        else:
            gp.add((b, a))
    goal_pairs = gp


def base_heuristic(_color_blocks_state):   # calculates this state's heuristic value, with a base heuristic.
    blocks, gp = _color_blocks_state.blocks, goal_pairs
    contains = gp.__contains__
    h, b = 0, blocks
    L = len(b)

    for i in range(L - 1):
        f1, s1 = b[i]
        f2, s2 = b[i + 1]
        if not ( contains((min(f1, f2), max(f1, f2))) or contains((min(f1, s2), max(f1, s2))) or
                 contains((min(s1, f2), max(s1, f2))) or contains((min(s1, s2), max(s1, s2))) ):
            h += 1
    return h


def advanced_heuristic(_color_blocks_state):   # calculates this state's heuristic value, with an advanced heuristic.
    b, gf, baseH = _color_blocks_state.blocks, goal_fronts, base_heuristic(_color_blocks_state)
    bonus = 0
    L = min(len(b), len(gf))

    for i in range(L):
        front, side = b[i]
        goal_front = gf[i]
        # We need one rotation to bring side -> front
        # but only if that side matches the target front.
        if front != goal_front and side == goal_front:
            bonus += 1

    return baseH + bonus
