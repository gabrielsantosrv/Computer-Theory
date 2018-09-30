def deep_first_search(graph):
    s = []
    visited = [False] * len(graph)

    # this loop considers disconnected graphs
    for i in range(len(visited)):
        if not visited[i]:
            DFS(s, visited, graph, i)

    return s


def DFS(s, visited, graph, v):
    visited[v] = True

    # it checks the neighbours
    for i in range(len(graph)):
        # if there is a path to another vertex and such vertex hasn't been visited yet,
        # go to this neighbour
        if (graph[v][i] == 1 and not visited[i]):
            DFS(s, visited, graph, i)

    s.append(v)


graph = [[0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0]]

# topological sort is DFS in reverse order
def topological_sort(graph):
    sorted_set = deep_first_search(graph)
    sorted_set.reverse()
    return sorted_set

print(topological_sort(graph))
