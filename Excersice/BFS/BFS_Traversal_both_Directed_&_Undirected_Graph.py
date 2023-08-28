from collections import deque


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


def bfs_traversal(graph, start_vertex, file):
    visited = [False] * (len(graph))
    queue = deque()

    visited[start_vertex] = True
    queue.append(start_vertex)
    print('queue:', queue)


    printing_graph = []
    while queue:
        pop_vertex = queue.popleft()
        printing_graph.append(str(pop_vertex))
        print('pop vertex:', pop_vertex)


        for neighbor in graph[pop_vertex]:
            print('neighbor:', neighbor)
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return file.write(" ".join(printing_graph))


# def print_bfs_graph(printed_graph, file):
#     file.write(" ".join(printed_graph))


#  Driver code

bfs_input_file = open('bfs_dir_undir_input.txt', 'r')
bfs_output_file = open('bfs_dir_undir_output.txt', 'w')

Graph = adjacency_graph_list(bfs_input_file, False)
start = 1
bfs_tra = bfs_traversal(Graph, start, bfs_output_file)

print(Graph)
print('BFS:', bfs_tra)