import heapq


def adjacency_graph_list(file, directed=True):
    vertex, edge = map(int, file.readline().split())

    adj_graph = [0] + [[] for i in range(vertex)]

    for i in range(edge):
        graph_value = list(map(int, file.readline().split()))

        vertex_1 = graph_value[0]
        vertex_2 = graph_value[1]
        weight = graph_value[2]

        adj_graph[vertex_1].append((vertex_2, weight))
        # if not directed:
        #     adj_graph[vertex_2].append(vertex_1)

    start_vertex = file.readline()
    # print(adj_graph)
    # print(start_vertex)
    return adj_graph, int(start_vertex)


def dijkstra(graph, start_vertex):
    distances = [float('inf')] * len(graph)
    distances[start_vertex] = 0

    min_heap_queue = [(0, start_vertex)]
    # print(min_heap_queue)

    while min_heap_queue:
        distance, vertex = heapq.heappop(min_heap_queue)

        if distance > distances[vertex]:
            continue
        # print('error point', graph[vertex])
        for neighbor, cost in graph[vertex]:
            new_distance = distances[vertex] + cost
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(min_heap_queue, (new_distance, neighbor))

    print(distances)
    return " ".join(map(str, distances[1:]))

def print_shortes_distance(distances, file):
    return file.write(distances)

input_file = open('input_1.txt', 'r')
output_file = open('output_1.txt', 'w')

Graph, Start = adjacency_graph_list(input_file)
minimum_distance = dijkstra(Graph, Start)
print(minimum_distance)
print_shortes_distance(minimum_distance, output_file)
