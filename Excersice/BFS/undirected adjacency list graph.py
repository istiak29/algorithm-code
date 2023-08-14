def adjacency_list(file):
    vertex, edge = (map(int, file.readline().split()))
    # print(vertex, type(vertex))
    # print(edge)

    #  creating empty adjaceency list which look like [0, [], [], [], [], []] \\ here the 0th index is ignored
    ad_graph_list = [0] + [[] for i in range(vertex)]

    for i in range(edge):
        graph_value = list(map(int, file.readline().split()))
        # print(graph_value)
        vertex_1 = graph_value[0]
        vertex_2 = graph_value[1]
        cost = graph_value[2]

        #  adding element to adjacency graph in vertex_1th index. The value of vertex_1th index is a tuple of (vertex_2, cost)
        ad_graph_list[vertex_1].append((vertex_2, cost))
        ad_graph_list[vertex_2].append((vertex_1, cost))

    # print(ad_graph_list)

    return ad_graph_list


def write_graph(graph, file):
    graph_output = ''

    for from_vertex in range(1, len(graph)):
        graph_output += f"{from_vertex} :"
        for to_neighbor in graph[from_vertex]:  # [(3, 4)]
            neighbor, cost = to_neighbor
            graph_output += f"({neighbor}, {cost})"
        graph_output += '\n'

    file.write(graph_output.strip())
    return graph_output


input_file = open('input_adList.txt', 'r')
output_file = open('output_Undirected_adList.txt', 'w')

Graph = adjacency_list(input_file)
print(Graph)
g = write_graph(Graph, output_file)
print(g)

input_file.close()
output_file.close()
