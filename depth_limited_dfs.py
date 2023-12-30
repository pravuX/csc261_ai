from queue import LifoQueue

graph = {
    "S": ("A", "D"),
    "A": ("B", "D", "S"),
    "B": ("A", "C", "E"),
    "C": ("B"),
    "D": ("A", "S", "E"),
    "E": ("D", "B", "F"),
    "F": ("E", "G"),
    "G": ("F"),
}

# graph = {
#     "S": ("A", "G"),
#     "A": ("B", "C"),
#     "B": ("D"),
#     "C": ("D", "G"),
#     "D": ("G"),
#     "G": (),
# }

# graph = {
#     "A": ("B", "C"),
#     "B": ("D", "E"),
#     "C": ("F", "G"),
#     "D": (),
#     "E": (),
#     "F": (),
#     "G": (),
# }


def dfs(source, destination, depth_limit):
    # create the search queue
    search_queue = LifoQueue()
    search_queue.put([source])
    # list of expanded/ visited vertices
    visited = []
    depth = 0
    while search_queue and depth <= depth_limit:
        print(list(search_queue.queue))
        path = search_queue.get()
        node = path[-1]
        depth += 1
        if not node in visited:
            visited.append(node)
            if node == destination:
                # show path
                print(f"Order of traversal: {', '.join(visited)}")
                print(f"Path: {' --> '.join(path)}")
                return True
            for child in graph[node]:
                search_queue.put(path + [child])
    return False


if __name__ == "__main__":
    d_limit = input("Enter the depth limit: ")
    if(not dfs("S", "G", int(d_limit))):
        print(f"Destination not found with within depth limit {d_limit}")
