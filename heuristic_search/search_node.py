
class search_node():     # Represents a node/state in the search tree of the search problem's solving.
    __slots__ = ("state", "g", "h", "f", "prev")  # to manually decrease allocation size of a search_node, for better Space Complexity.
    def __init__(self, state, g=0, h=0, prev=None):
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h
        self.prev = prev

    def __lt__(self, other):         # the heap depends on this to decide which node/state/neighbor is better.
        if self.f != other.f:
            return self.f < other.f
        return self.h < other.h

    def get_neighbors(self):
        return self.state.get_neighbors()
