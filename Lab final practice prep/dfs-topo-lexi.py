import heapq

def dfs_topological_sort(graph, node, visited, heap):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_topological_sort(graph, neighbor, visited, heap)
    heapq.heappush(heap, node)

def topological_sort(graph, num_nodes):
    visited = [False] * (num_nodes + 1)
    heap = []
    for node in range(1, num_nodes + 1):
        if not visited[node]:
            dfs_topological_sort(graph, node, visited, heap)
    return heap

def read_graph(input_file):
    num_nodes, num_edges = map(int, input_file.readline().split())
    graph = [[] for _ in range(num_nodes + 1)]
    for _ in range(num_edges):
        u, v = map(int, input_file.readline().split())
        graph[u].append(v)
    return graph, num_nodes

def write_topological_order(order, output_file):
    for node in order:
        output_file.write(str(node) + " ")
    output_file.write("\n")

input_file = open("input.txt", "r")
output_file = open("output.txt", "w")

graph, num_nodes = read_graph(input_file)
topological_order = topological_sort(graph, num_nodes)
write_topological_order(topological_order, output_file)

input_file.close()
output_file.close()
