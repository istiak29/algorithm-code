import heapq

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [0] + [[] for _ in range(n)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))  # Adding edge from u to v with weight w

    def dijkstra(self):
        distances = [float('inf')] * self.n
        max_danger = [0] * self.n
        distances[0] = 0

        heap = [(0, 0)]  # (distance, node)

        while heap:
            dist, node = heapq.heappop(heap)

            if dist > distances[node]:
                continue

            for neighbor, danger in self.graph[node]:
                new_dist = max(distances[node], danger)
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    max_danger[neighbor] = max(max_danger[node], danger)
                    heapq.heappush(heap, (distances[neighbor], neighbor))

        return max_danger[self.n - 1], distances[self.n - 1]

# Read input from file
with open("gpt_input.txt", "r") as input_file:
    N, M = map(int, input_file.readline().split())
    graph = Graph(N)

    for _ in range(M):
        u, v, w = map(int, input_file.readline().split())
        graph.add_edge(u, v, w)  # Use original node numbering

# Find the minimum danger level
min_danger, min_dist = graph.dijkstra()

# Write output to file
with open("gpt_output.txt", "w") as output_file:
    if min_dist == float('inf'):
        output_file.write("Impossible\n")
    else:
        output_file.write(str(min_danger) + "\n")
