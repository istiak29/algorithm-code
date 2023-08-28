def read_graph(input_file):
    vertex, edge = map(int, input_file.readline().split())
    
    graph_list = [0] + [[] for i in range(vertex)]
    
    for i in range(edge):
        u, v = map(int, input_file.readline().split())
        
        graph_list[u].append(v)
        
    return graph_list, vertex


def dfs_topological_sort(graph, node, visited, stack):
    visited[node] = True
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_topological_sort(graph, neighbor, visited, stack)
    
    stack.append(node)
    

def topological_sort(graph, vertex):
    visited = [False] * (vertex + 1)
    
    stack = []
    
    for neighbor in range(1, vertex + 1):
        if not visited[neighbor]:
            dfs_topological_sort(graph, neighbor, visited, stack)
    
    return[::-1]