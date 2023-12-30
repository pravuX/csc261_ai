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

# John Levine Example Graph
# https://www.youtube.com/watch?v=dRMvK76xQJI
# graph = {
#     "S": {(5, "A"), (6, "D"), (9, "B")},
#     "A": {(3, "B"), (9, "G")},
#     "B": {(2, "A"), (1, "C")},
#     "C": {(6, "S"), (5, "G"), (7, "F")},
#     "D": {(1, "S"), (2, "C"), (2, "E")},
#     "E": {(7, "G")},
#     "F": {(2, "D")},
#     "G": {},
# }

# directed graph

# graph = {
#     "S": {(1, "A"), (12, "G")},
#     "A": {(3, "B"), (1, "C")},
#     "B": {(3, "D")},
#     "C": {(1, "D"), (2, "G")},
#     "D": {(3, "G")},
#     "G": {},
# }


def show_traversed_nodes(visited_arr):
    # when passing visited
    order = "Order of Traversal: "
    order += ", ".join(visited_arr)
    print(order)


def uniform_cost(source, destination):
    # search queue is a priority queue ordered by path total_cost
    # it stores the frontier
    search_queue = PriorityQueue()
    # (total path cost from source, path from source as a list)
    search_queue.put((0, [source]))

    # list of expanded/ visited vertices
    visited = []

    while search_queue:
        # total_cost = total cost of the currently expanded node from source
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
                    # path total_cost = total_cost of current node(parent) + total_cost of path to child
                    search_queue.put((total_cost + cost, current_path + [child]))
    return False


if __name__ == "__main__":
    uniform_cost("S", "G")
