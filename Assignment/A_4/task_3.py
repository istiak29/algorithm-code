from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def edge_add(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def Depth_First_Search_DFS(self, node_start, visited, output_file):
        visited[node_start] = True
        with open(output_file, "a") as file:
            file.write(str(node_start) + " ")

        for neighbor in self.graph[node_start]:
            if not visited[neighbor]:
                self.Depth_First_Search_DFS(neighbor, visited, output_file)


def graph_read(input_file):
    graph = Graph()
    with open(input_file, "r") as file:
        nodes, edges = map(int, file.readline().split())
        for i in range(edges):
            x, y = map(int, file.readline().split())
            graph.edge_add(x, y)
    return graph


def traversal_DFS(g, node_start, output_file):
    visited = [False] * (len(g.graph) + 1)
    g.Depth_First_Search_DFS(node_start, visited, output_file)


input_file = "input_3.txt"
output_file = "output_3.txt"

g = graph_read(input_file)
start = 1
traversal_DFS(g, start, output_file)
