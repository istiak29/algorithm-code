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

    start_vertex_1, start_vertex_2 = map(int, file.readline().split())

    return adj_graph, int(start_vertex_1), int(start_vertex_2)


def dijkstra(graph, start_vertex):
    distances = [float('inf')] * len(graph)
    distances[start_vertex] = 0

    min_heap_queue = [(0, start_vertex)]
    # print(min_heap_queue)
    print(graph)
    while min_heap_queue:
        distance, vertex = heapq.heappop(min_heap_queue)
        print('vertex-',vertex)

        if distance > distances[vertex]:
            continue
        # print('error point', graph[vertex])
        for neighbor, cost in graph[vertex]:
            print('neighbor',neighbor)
            print('cost-', cost)
            new_distance = distances[vertex] + cost
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(min_heap_queue, (new_distance, neighbor))

    return distances


def minimum_time_amount(graph, min_time_1, min_time_2):
    distance_1 = dijkstra(graph, min_time_1)
    # print('d1=', distance_1)
    distance_2 = dijkstra(graph, min_time_2)
    # print('d2=', distance_2)

    meet_time = 0
    meet_node = None
    total_time = False

    for dis in range(1, len(distance_1)):
        if distance_1[dis] != float('inf') and distance_2[dis] != float('inf'):
            time = distance_1[dis] + distance_2[dis]

            if not total_time:
                total_time = time
                meet_time = max(distance_1[dis], distance_2[dis])
                meet_node = dis

    if not total_time:
        return 'Impossible'

    return f"Time {meet_time} \nNode {meet_node}"


input_file = open('input_2.txt', 'r')
output_file = open('output_2.txt', 'w')

Graph, Start_1, Start_2 = adjacency_graph_list(input_file)

Meet_Node_Time = minimum_time_amount(Graph, Start_1, Start_2)

output_file.write(Meet_Node_Time)

input_file.close()
output_file.close()