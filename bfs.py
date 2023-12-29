from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": [],
}


def is_destination(v, d):
    if v == d:
        return True
    return False


def show_path(source, visited_arr, destination):
    path = ""
    path += f"{source} --> "
    for v in visited_arr:
        path += f"{v} --> "
    path += f"{destination}"
    print(path);


def bfs(source, destination):
    # create the search queue
    search_queue = deque()
    search_queue += graph[source]
    # list of expanded/ visited vertices
    visited = []

    while search_queue:
        vertex = search_queue.popleft()
        if not vertex in visited:
            if is_destination(vertex, destination):
                show_path(source, visited, destination)
                return True
            else:
                search_queue += graph[vertex]
                visited.append(vertex)
    return False


if __name__ == "__main__":
    bfs("A", "E")
