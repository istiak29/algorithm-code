def adjacency_graph_list(file):
    vertex, edge = list(map(int, file.readline().split()))
    # print('vertex:', vertex)
    # print('edge:', edge)
    adj_graph_list = [0] + [[] for i in range(vertex)]
    
    for i in range(edge):
        value = list(map(int, file.readline().split()))
        
        node_from = value[0]
        node_to = value[1]
        weight = value[2]
        
        adj_graph_list[node_from].append((node_to, weight))
        
    return adj_graph_list

def print_graph(graph, file):
    output = ''
    
    for i in range(1, len( graph)):
        print(i)
        output += f"{i} :"
        for j in graph[i]:
            
            print('j:', j)
            
            val_1, val_2 = j
            
            print('val_1:', val_1)
            print('val_2:', val_2)
            
            output += f"{val_1},{val_2} "
        
        output += '\n'
    
    file.write(output.strip())
    
    return output
    
        


input_file = open('input_1b.txt', 'r')
output_file = open('output1b.txt', 'w')



adj_graph = adjacency_graph_list(input_file)
print(adj_graph)

graph_str = print_graph(adj_graph, output_file)        

print(graph_str)