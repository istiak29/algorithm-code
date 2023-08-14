import heapq


def adjacency_graph_list(file, directed=True):
    vertex, edge = map(int, file.readline().split())

    adj_graph = [[] for i in range(vertex)]

    for i in range(edge):
        graph_value = list(map(int, file.readline().split()))

        vertex_1 = graph_value[0]
        vertex_2 = graph_value[1]
        weight = graph_value[2]

        adj_graph[vertex_1-1].append((vertex_2-1, weight))
        # if not directed:
        #     adj_graph[vertex_2].append(vertex_1)

    # start_vertex, destination = map(int, file.readline().split())

    return adj_graph


def dijkstra(graph, start):
    distances = [float('inf')] * len(graph)
    min_danger = [0] * len(graph)
    distances[0] = 0

    print('graph len =', len(graph))

    heap_list = [(0, start-1)]
    print(graph)

    while heap_list:
        distance, vertex = heapq.heappop(heap_list)
        print(graph[vertex])

        if distance > distances[vertex]:
            continue

        for neighbor, danger in graph[vertex]:
            new_distance = max(distances[vertex], danger)
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                min_danger[neighbor] = max(min_danger[vertex], danger)
                heapq.heappush(heap_list, (distances[neighbor], neighbor))

    print('danger-min',min_danger)
    print('dis_min-', distances)
    return min_danger[len(graph)-1], distances[len(graph)-1]


def print_safe_path(min_danger, min_distance, file):
    if min_distance == float('inf'):
        file.write('Impossible')
    else:
        print('min_danger-', min_danger)
        file.write(str(min_danger))


input_file = open('input_3.txt', 'r')
output_file = open('output_3.txt', 'w')

Graph = adjacency_graph_list(input_file)
Start = 1
minimum_danger, minimum_distance = dijkstra(Graph, Start)

print_safe_path(minimum_danger, minimum_distance, output_file)

input_file.close()
output_file.close()
