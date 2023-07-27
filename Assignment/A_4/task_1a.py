def print_graph(graph, output_file):
    result = ''

    for i in range(1, len(graph)):
        temp = list(map(str, graph[i]))
        result += ' '.join(temp) + '\n'

    output_file.write(result.strip())


def adjacency_matrix(input_file):
    vertice, edge = list(map(int, input_file.readline().split()))

    graphlist = [0] + [[0 for i in range(vertice)] for i in range(vertice)]

    for i in range(edge):
        value = list(map(int, input_file.readline().split()))

        node_1 = value[0]
        node_2 = value[1]
        weight_value = value[2]

        graphlist[node_1][node_2 - 1] = weight_value

    return graphlist


input_file = open("input_1a.txt", "r")
output_file = open("output_1a.txt", "w")

graph = adjacency_matrix(input_file)
print_graph(graph, output_file)

input_file.close()
output_file.close()
