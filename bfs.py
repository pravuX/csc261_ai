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


def bfs(source, destination):
    # create the search queue
    search_queue = deque()
    search_queue.append(source)
    # list of expanded/ visited vertices
    visited = []

    while search_queue:
        node = search_queue.popleft()
        if not node in visited:
            visited.append(node)
            if node == destination:
                # show path
                print(f"Path: {' --> '.join(visited)}")
                return True
            else:
                search_queue += graph[node]
    return False


if __name__ == "__main__":
    bfs("S", "G")
