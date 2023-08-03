input_file = open("input_1a.txt", "r")
output_file = open("output_1a.txt", "w")

number_of_course, prerequest = list(map(int, input_file.readline().split()))

graph_list = []

for i in range(number_of_course + 1):
    temp_1 = []
    graph_list.append(temp_1)
for j in range(prerequest):
    temp_2 = input_file.readline().split()
    c_1, c_2 = int(temp_2[0]), int(temp_2[1])
    graph_list[c_1].append(c_2)

if number_of_course < prerequest:
    visited = [0] * (prerequest + 1)
elif prerequest < number_of_course:
    visited = [0] * (number_of_course + 1)
else:
    visited = [0] * (number_of_course + 1)

order_list = []
flag = False


def dfs(value, visited):
    if visited[value] == -1:
        return False
    if visited[value] == 1:
        return True
    visited[value] = -1
    for n in graph_list[value]:
        if not dfs(n, visited):
            return False
    order_list.append(value)
    visited[value] = 1
    return True


for n in range(1, number_of_course + 1):
    if not dfs(n, visited):
        flag = True
if flag:
    print('IMPOSSIBLE', file=output_file)
else:
    print(order_list[::-1], file=output_file)

output_file.close()
