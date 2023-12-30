from queue import PriorityQueue

# unidrected

graph = {
    "S": {(6, "A"), (3, "D")},
    "A": {(5, "B"), (5, "D"), (6, "S")},
    "B": {(5, "A"), (4, "C"), (5, "E")},
    "C": {(4, "B")},
    "D": {(5, "A"), (3, "S"), (2, "E")},
    "E": {(2, "D"), (5, "B"), (4, "F")},
    "F": {(4, "E"), (3, "G")},
    "G": {(3, "F")},
}
heuristics = {
    "S": 12,
    "A": 8,
    "B": 7,
    "C": 5,
    "D": 9,
    "E": 4,
    "F": 2,
    "G": 0,
}

# directed graph

# graph = {
#     "S": {(1, "A"), (12, "G")},
#     "A": {(3, "B"), (1, "C")},
#     "B": {(3, "D")},
#     "C": {(1, "D"), (2, "G")},
#     "D": {(3, "G")},
#     "G": {},
# }
# heuristics = {
#     "S": 4,
#     "A": 2,
#     "B": 6,
#     "C": 2,
#     "D": 3,
#     "G": 0,
# }


def show_traversed_nodes(visited_arr):
    order = "Order of Traversal: "
    order += ", ".join(visited_arr)
    print(order)


def a_star(source, destination):
    # search queue is a priority queue ordered by path total_cost
    # it stores the frontier
    search_queue = PriorityQueue()
    # (heuristic + total path cost from source, path from source as a list)
    search_queue.put((heuristics[source] + 0, [source]))

    # list of expanded/ visited vertices
    visited = []

    while search_queue:
        # total_cost = total cost of the currently expanded node from source + heuristic value of that node
        # current_path = list of nodes from source to currently expanded node
        print(search_queue.queue)
        total_cost, current_path = search_queue.get()
        current_node = current_path[-1]  # last node in the current_path
        if not current_node in visited:
            visited.append(current_node)
            # when a goal state is visited
            if current_node == destination:
                # using a priority queue ensures that the
                # goal state reached will have followed the
                # most optimal path (i.e. shortest path)
                show_traversed_nodes(visited)
                # show the shortest path and it's cost
                print(f"Cost: {total_cost}\nPath: {' --> '.join(current_path)}")
                return True
            # expand the node for visiting
            for cost, child in graph[current_node]:
                if not child in current_path:
                    # f = h + g
                    # cost = path cost from parent to child
                    parent_path_cost = total_cost - heuristics[current_node] # from source
                    child_path_cost = parent_path_cost + cost # from source
                    search_queue.put((heuristics[child] + child_path_cost, current_path + [child]))
    return False


if __name__ == "__main__":
    a_star("S", "G")
