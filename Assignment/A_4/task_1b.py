def print_graph(graph, output_file):
    result = ''

    for i in range(1, len(graph)):
        result += f'{i} :'
        for j in graph[i]:
            x, y = j
            result += f' ({x},{y})'
        result += '\n'

    output_file.write(result.strip())

    return result


def adjacency_list(input_file):
    vertice, edge = list(map(int, input_file.readline().split()))

    graph_list = [0] + [[] for i in range(vertice)]

    for i in range(edge):
        value = list(map(int, input_file.readline().split()))

        node_1 = value[0]
        node_2 = value[1]
        weight_value = value[2]

        graph_list[node_1].append((node_2, weight_value))

    return graph_list


input_file = open("input_1b.txt", "r")
output_file = open("output_1b.txt", "w")

Graph = adjacency_list(input_file)
graph_str = print_graph(Graph, output_file)

print(Graph)
print(graph_str)

input_file.close()
output_file.close()
