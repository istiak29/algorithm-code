def adjacency_list(input_file):
    vertex, edge = list(map(int, input_file.readline().split()))

    graph_list = [0] + [[] for i in range(vertex)]

    for i in range(edge):
        value = list(map(int, input_file.readline().split()))

        node_1 = value[0]
        node_2 = value[1]

        graph_list[node_1].append((node_2))

    return graph_list


def find_cycle_DFS(graph, visited=None, st_node=1, cycle=False):
    if visited is None:
        visited = [None for i in range(len(graph))]

    visited[st_node] = 2
    # print(visited)

    for c in graph[st_node]:

        if visited[c] is None:
            cycle = find_cycle_DFS(graph, visited, c, cycle)

        elif visited[c] == 2:
            return True

        if cycle:
            return cycle

    visited[st_node] = 1
    return cycle


input_file = open("input_4.txt", "r")
output_file = open("output_4.txt", "w")

Graph = adjacency_list(input_file)

if find_cycle_DFS(Graph):
    output_file.write('Yes')

else:
    output_file.write('No')



input_file.close()
output_file.close()
