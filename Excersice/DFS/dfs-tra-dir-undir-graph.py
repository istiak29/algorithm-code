def adjacency_graph_list(file, directed=True):
    vertex, edge = map(int, file.readline().split())

    adj_graph = [0] + [[] for i in range(vertex)]

    for i in range(edge):
        graph_value = list(map(int, file.readline().split()))

        vertex_1 = graph_value[0]
        vertex_2 = graph_value[1]

        adj_graph[vertex_1].append(vertex_2)
        if not directed:
            adj_graph[vertex_2].append(vertex_1)

    return adj_graph


def dfs_processing(graph, start_vertex, visited, output_file):
    visited[start_vertex] = True

    with open(output_file, 'a') as file:
        file.write(str(start_vertex) + " ")

    for neighbor in graph[start_vertex]:
        if not visited[start_vertex]:
            dfs_processing(graph, neighbor, visited, output_file)


def dfs_traversal(graph, start_vertex, output_file):
    visited = [False] * len(graph)
    dfs_processing(graph, start_vertex, visited, output_file)


# Driver code
input_file_DFS = open('input_dfs_dir_undir.txt', 'r')
output_file_DFS = open('output_dfs_dir_undir.txt', 'w')

Graph = adjacency_graph_list(input_file_DFS, False)
start = 1
dfs_traversal(Graph, start, output_file_DFS)
