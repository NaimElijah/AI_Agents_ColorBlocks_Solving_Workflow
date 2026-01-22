from heuristic_search.color_blocks_state import color_blocks_state
from heuristic_search.search_node import search_node
import heapq

def create_open_set():
    open_heap = []
    heapq.heapify(open_heap)    # ordered by f value, with the highest priority state being with lowest f value, min-heap.
    open_map = {}               # state -> node pairs(with best g so far)
    return open_heap, open_map


def create_closed_set():
    return {}              # state -> node pairs


def add_to_open(vn, open_set):
    heapq.heappush(open_set[0], vn)
    open_set[1][vn.state] = vn


def open_not_empty(open_set):
    return len(open_set[0]) > 0


def get_best(open_set):
    heap, mp = open_set
    while heap:
        node = heapq.heappop(heap)
        # Skip if this entry is outdated/not in the map that holds the best ones.
        if node.state in mp and mp[node.state] is node:   # and if it's the updated one, return it.
            del mp[node.state]
            return node
    return None   # should never get here unless OPEN was corrupted.



def add_to_closed(vn, closed_set):
    closed_set[vn.state] = vn



#returns False if curr_neighbor state not in open_set or has a lower g from the node in open_set
#remove the node with the higher g from open_set (if exists)
def duplicate_in_open(vn, open_set):
    heap, mp = open_set
    if vn.state not in mp:
        return False  # no duplicate
    existing = mp[vn.state]
    # If existing g is LOWER than new g that means that existing path is better.
    if existing.g <= vn.g:
        return True  # discard vn
    # If got to here so: vn is BETTER, remove old, replace with new
    del mp[vn.state]
    # old entry stays in heap, but will be ignored, so it's ok.
    # and after this in the search we will(also depends on the second predicate) add the new one.
    return False




#returns False if curr_neighbor state not in closed_set or has a lower g from the node in closed_set
#remove the node with the higher g from closed_set (if exists)
def duplicate_in_closed(vn, closed_set):
    if vn.state not in closed_set:
        return False
    existing = closed_set[vn.state]
    if existing.g <= vn.g:
        return True  # existing is better, discard/ignore vn(the new)
    # If got to here so: remove old one (reopen)
    del closed_set[vn.state]
    # and after this in the search we will(also depends on the second predicate) add the new one.
    return False



# helps to debug sometimes..
def print_path(path):
    for i in range(len(path)-1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(f"[{path[-1].state.get_state_str()}]")


def search(start_state, heuristic):

    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):

        current = get_best(open_set)    # get the neighbor/state with the lowest cost.

        if color_blocks_state.is_goal_state(current.state):
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path

        add_to_closed(current, closed_set)     # because we just chose and expanded this scenario/state.

        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None


