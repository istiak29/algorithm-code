from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def bfs(self, start_vertex):
        visited = [False] * (self.vertices + 1)
        queue = deque()

        visited[start_vertex] = True
        queue.append(start_vertex)

        result = []
        while queue:
            vertex = queue.popleft()
            result.append(str(vertex))

            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result

    def read_graph(self, input_file):
        with open(input_file, "r") as f:
            self.vertices, edges = map(int, f.readline().split())
            for _ in range(edges):
                u, v = map(int, f.readline().split())
                self.add_edge(u, v)

    def write_bfs_traversal(self, start_vertex, output_file):
        result = self.bfs(start_vertex)
        with open(output_file, "w") as f:
            f.write(" ".join(result))


# Usage
input_file = "input_BFS_Tra_Undirected.txt"
output_file = "output_BFS_Tra_Undirected.txt"

# Create a Graph instance
graph = Graph(0)

# Read the graph from the input file
graph.read_graph(input_file)

# Perform BFS traversal starting from vertex 1
result = graph.bfs(1)

# Write the BFS traversal to the output file
graph.write_bfs_traversal(1, output_file)
