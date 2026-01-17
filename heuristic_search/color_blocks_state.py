import re

def init_goal_for_search(goal_blocks):
    # setting the goal
    color_blocks_state.goal_state = [int(x) for x in goal_blocks.split(",")]


class color_blocks_state:
    goal_state = []

    def __init__(self, blocks_str, **kwargs):
        # construct from a list of tuples.
        if "blocks_list" in kwargs:
            self.blocks = list(kwargs["blocks_list"])
            self.n = len(self.blocks)
            return
        # construct from the blocks_str arg.
        nums = re.findall(r'-?\d+', blocks_str)
        nums = [int(x) for x in nums]
        self.blocks = [(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)]
        self.n = len(self.blocks)


    @staticmethod
    def is_goal_state(_color_blocks_state):
        if len(_color_blocks_state.blocks) != len(color_blocks_state.goal_state):
            return False

        for i, (front, side) in enumerate(_color_blocks_state.blocks):
            if front != color_blocks_state.goal_state[i]:
                return False

        return True


    def get_neighbors(self):   # gets all possible states from this state after making one operation (rotating or flipping)
        b, n, neighbors = self.blocks, self.n, []

        # States/neighbors reachable from rotating a single cube.
        for i in range(n):
            blocks_copy = list(b)
            front, side = blocks_copy[i]
            blocks_copy[i] = (side, front)  # swap
            neighbors.append((color_blocks_state("", blocks_list=blocks_copy), 1))

        # States/neighbors reachable from flipping a subset of cubes from the bottom.
        for k in range(2, n + 1):  # flipping bottom-1 cube is meaningless
            blocks_copy = list(b)
            bottom_part = blocks_copy[-k:]
            bottom_part.reverse()
            blocks_copy = blocks_copy[:-k] + bottom_part
            neighbors.append((color_blocks_state("", blocks_list=blocks_copy), 1))
        return neighbors


    def __hash__(self):
        return hash(tuple(self.blocks))

    def __eq__(self, other):
        if not isinstance(other, color_blocks_state):
            return False
        return self.blocks == other.blocks

    # for debugging states
    def get_state_str(self):
        return ",".join(f"({a},{b})" for (a, b) in self.blocks)
