from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def edge_add(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bredth_first_search_BFS(self, node_start, output_file):
        visited = set()
        queue = deque()

        visited.add(node_start)
        queue.append(node_start)

        with open(output_file, "w") as file:
            while queue:
                node_current = queue.popleft()
                file.write(str(node_current) + " ")

                for neighbor in self.graph[node_current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)


# Function to read input graph from a file
def graph_read(input_file):
    graph = Graph()
    with open(input_file, "r") as file:
        num_nodes, num_edges = map(int, file.readline().split())
        for i in range(num_edges):
            x, y = map(int, file.readline().split())
            graph.edge_add(x, y)
    return graph


# Example usage with input and output files
input_file = "input_2.txt"
output_file = "output_2.txt"

graph = graph_read(input_file)
start = 1
graph.bredth_first_search_BFS(start, output_file)

# print("BFS traversal completed. Result is saved in 'output.txt'.")
