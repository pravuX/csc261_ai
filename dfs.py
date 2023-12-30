from collections import deque

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
#     "A": ("C", "B"),
#     "B": ("E", "D"),
#     "C": ("G", "F"),
#     "D": (),
#     "E": (),
#     "F": (),
#     "G": (),
# }


def dfs(source, destination):
    # create the search queue
    search_queue = deque()
    search_queue.append(source)
    # list of expanded/ visited vertices
    visited = []

    while search_queue:
        print(list(search_queue))
        node = search_queue.pop()
        if not node in visited:
            visited.append(node)
            if node == destination:
                # show path
                print(f"Path: {' --> '.join(visited)}")
                return True
            search_queue += graph[node]
    return False


if __name__ == "__main__":
    dfs("S", "G")
