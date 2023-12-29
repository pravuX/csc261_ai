from queue import PriorityQueue

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


def add_children_of(node, q):
    for cost, child in graph[node]:
        heuristic = heuristics[child]
        q.put((heuristic, cost, child))


def gbfs(source, destination):
    # search queue is a priority queue ordered by path cost
    # it stores the frontier
    search_queue = PriorityQueue()
    # heuristic, cost, node
    # cost can be removed if the total cost of the path between
    # source and destination is not required
    search_queue.put((heuristics[source], 0, source))
    add_children_of(source, search_queue)
    # list of expanded/ visited vertices
    visited = []
    # this is not needed in uniform_cost because the PriorityQueue orders
    # based on total path cost from source, which for the source
    # node is always going to be zero so is it expanded first but
    # here it is necessary to mark the source node as visited and add its
    # children to the PriorityQueue before executing the gbfs algorithm
    visited.append((0, source))
    total_cost = 0
    while search_queue:
        _, cost, node = search_queue.get()
        if not node in visited:
            visited.append((cost, node))
            if node == destination:
                path = ' -> '.join([node for _, node in visited])
                for cost, node in visited:
                    total_cost += cost
                print(f"Cost: {total_cost}\nPath: {path}")
                return True
            add_children_of(node, search_queue)
    return False


if __name__ == "__main__":
    gbfs("S", "G")
