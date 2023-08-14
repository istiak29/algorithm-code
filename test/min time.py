from queue import PriorityQueue


def buildGraphUsingAdjacencyList(file_input):
    vertices, edges = list(map(int, file_input.readline().split()))
    listGraph = [0] + [{} for i in range(vertices)]

    for i in range(edges):
        node_from, node_to, weight = list(map(int, file_input.readline().split()))
        listGraph[node_from][node_to] = weight

    person1, person2 = list(map(int, file_input.readline().split()))
    return listGraph, person1, person2


def shortestPathUsingDijkstra(graph, start):
    distance = [-1 for i in range(len(graph))]
    Q = PriorityQueue()

    distance[start] = 0
    Q.put((0, start))

    while not Q.empty():
        curr_weight, curr_node = Q.get()

        for child, weight in graph[curr_node].items():

            alternate = weight + curr_weight

            if distance[child] == -1:
                distance[child] = alternate
                Q.put((alternate, child))

            elif alternate < distance[child]:
                distance[child] = alternate
                Q.put((alternate, child))
    print(distance)
    return distance


def minimumTime(graph, person1, person2):
    distances1 = shortestPathUsingDijkstra(graph, person1)
    distances2 = shortestPathUsingDijkstra(graph, person2)

    total_time, time, node = None, None, None

    for i in range(1, len(distances1)):

        if distances1[i] != -1 and distances2[i] != -1:

            curr_time = distances1[i] + distances2[i]

            if total_time is None:
                total_time = curr_time
                time = max(distances1[i], distances2[i])
                node = i

            elif curr_time < total_time:
                total_time = curr_time
                time = max(distances1[i], distances2[i])
                node = i

    if total_time is None:
        return 'Impossible'

    return f'Time {time}\nNode {node}'


file_input = open("input2_1.txt", "r")
file_output = open("output2_1.txt", "w")

graph, person1, person2 = buildGraphUsingAdjacencyList(file_input)
result = minimumTime(graph, person1, person2)
file_output.write(result)

file_input.close()
file_output.close()