from collections import deque

def adjacency_graph_list(file, directed=False):
    vertex, edge = map(int, file.readline().split())
    
    adj_graph = [0] + [[] for i in range(vertex)]
    
    for i in range(edge):
        graph_value = list(map(int, file.readline().split()))
        
        from_vertex = graph_value[0]
        to_vertex = graph_value[1]
        
        # weight = graph_value[2]
        
        # adj_graph[from_vertex].append((to_vertex, weight))
        
        # if directed != True:
        #     adj_graph[to_vertex].append((from_vertex, weight))
            
    return adj_graph


def BFS_traversal(graph, sVertex, file):
    visited = [False] * (len(graph))
    queue = deque()
    
    visited[sVertex] = True
    
    queue.append(sVertex)
    
    printed_Graph = []
    print('queue:', queue)
    
    while queue:
        pop_vertex = queue.popleft()
        print('pop vertex:', pop_vertex)
        printed_Graph.append(str(pop_vertex))
        
        for neighbor in graph[pop_vertex]:
            print('neighbor:', neighbor)
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    file.write('\n\n')
    file.write(''.join(printed_Graph))
    return printed_Graph

def print_graph(graph, file):
    output = ''
    
    for i in range(1, len(graph)):
        output += f"{i} :"
        for j in graph[i]:
            x, y = j
            
            output += f"({x}, {y})"
        output += f"\n"
    
    file.write(output)
    return output


input_file = open('input-bfs-rep-tra-dir-undir.txt', 'r')
output_file = open('output-bfs-rep-tra-dir-undir.txt', 'a')


graph = adjacency_graph_list(input_file)
adjGraph = print_graph(graph, output_file)

print(graph)
print(adjGraph)

# BFS traversal
traversal = BFS_traversal(graph, 1, output_file)

print(traversal)