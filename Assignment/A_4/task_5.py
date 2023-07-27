
import queue


def adjacency_list(file_input):
    vertice, edge, target = list(map(int, file_input.readline().split()))

    graph_list = [0] + [[] for i in range(vertice)]

    for i in range(edge):
        value = list(map(int, file_input.readline().split()))

        node_1 = value[0]
        node_2 = value[1]

        graph_list[node_1].append((node_2))
        graph_list[node_2].append((node_1))

    return graph_list, target


def find_shortest_path_bfs(graph, target):
    visited = [None for i in range(len(graph))]
    queue_lsit = queue.Queue(maxsize=len(graph))

    visited[1] = 0
    queue_lsit.put(1)

    while not queue_lsit.empty():
        node_current = queue_lsit.get()

        if node_current is target:
            c_time = -1
            city_path = ''

            while node_current != 0:
                c_time += 1
                city_path = f'{node_current} ' + city_path
                node_current = visited[node_current]

            return f'Time: {c_time}\nShortest Path: {city_path.strip()}'

        for c in graph[node_current]:

            if visited[c] is None:
                visited[c] = node_current
                queue_lsit.put(c)

    return


input_file = open("input_5.txt", "r")
output_file = open("output_5.txt", "w")

graph, target = adjacency_list(input_file)
output_file.write(find_shortest_path_bfs(graph, target))

input_file.close()
output_file.close()
