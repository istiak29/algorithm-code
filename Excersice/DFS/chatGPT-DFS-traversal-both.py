class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices + 1)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        # For undirected graph
        # self.graph[v].append(u)

    def dfs(self, vertex, visited):
        result = []

        stack = [vertex]
        visited[vertex] = True

        while stack:
            v = stack.pop()
            result.append(str(v))

            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True

        return result

    def dfs_traversal(self, start_vertex):
        visited = [False] * (self.vertices + 1)
        return self.dfs(start_vertex, visited)

    def read_graph(self, input_file):
        with open(input_file, "r") as f:
            self.vertices, edges = map(int, f.readline().split())
            for _ in range(edges):
                u, v = map(int, f.readline().split())
                self.add_edge(u, v)

    def write_dfs_traversal(self, start_vertex, output_file):
        result = self.dfs_traversal(start_vertex)
        with open(output_file, "w") as f:
            f.write(" ".join(result))


# Usage
input_file = "inputGPT.txt"
output_file = "outputGPT.txt"

# Create a Graph instance
graph = Graph(0)

# Read the graph from the input file
graph.read_graph(input_file)

# Perform DFS traversal starting from vertex 1
graph.write_dfs_traversal(1, output_file)
