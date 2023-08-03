from collections import defaultdict

input_file = open("input_3.txt", "r")
output_file = open("output_3.txt", "w")

dict_1 = defaultdict(list)
dict_2 = defaultdict(list)

vertex, edge = list(map(int, input_file.readline().split()))

for i in range(edge):
    graph_list = input_file.readline().split()
    v1, v2 = int(graph_list[0]), int(graph_list[1])
    dict_1[v1].append(v2)


def dfs(n1, visited_1):
    visited_1[n1] = True
    print(n1, file=output_file)
    for i in dict_1[n1]:
        if not visited_1[i]:
            dfs(i, visited_1)


def order(n2, visited_2, stack):
    visited_2[n2] = True
    for i in dict_1[n2]:
        if not visited_2[i]:
            order(i, visited_2, stack)
    stack = stack.append(n2)


def transpose():
    for i in dict_1:
        for j in dict_1[i]:
            dict_2[j] = i
    return dict_2


def strongly_connected():
    stack = []
    visited_3 = [False] * (vertex + 1)
    for i in range(1, vertex + 1):
        if not visited_3[i]:
            order(i, visited_3, stack)
    temp = transpose()
    visited_4 = [False] * (vertex + 1)

    while stack:
        n = stack.pop()
        if not visited_4[n]:
            dfs(n, visited_4)


strongly_connected()

output_file.close()
