from queue import PriorityQueue


def buildGraphUsingAdjacencyList(file_input):
    vertices, edges = list(map(int, file_input.readline().split()))
    listGraph = [0] + [{} for i in range(vertices)]

    for i in range(edges):
        node_from, node_to, weight = list(map(int, file_input.readline().split()))
        listGraph[node_from][node_to] = weight

    return listGraph, 1, vertices


def safestPathUsingDijkstra(graph, start, end):
    distance = [-1 for i in range(len(graph))]
    Q = PriorityQueue()

    distance[start] = 0
    Q.put((0, start))

    print(graph)
    while not Q.empty():
        curr_weight, curr_node = Q.get()

        for child, weight in graph[curr_node].items():

            if child == end:

                alternative = max(curr_weight, weight)

                if distance[child] == -1:
                    distance[child] = alternative
                    Q.put((alternative, child))

                elif alternative < distance[child]:
                    distance[child] = alternative
                    Q.put((alternative, child))


            elif distance[child] == -1:
                distance[child] = weight
                Q.put((weight, child))

            elif weight < distance[child]:
                distance[child] = weight
                Q.put((weight, child))

    return distance[end]


file_input = open("input3.txt", "r")
file_output = open("output3.txt", "w")

graph, start, end = buildGraphUsingAdjacencyList(file_input)
danger = safestPathUsingDijkstra(graph, start, end)
file_output.write(str(danger))

file_input.close()
file_output.close()