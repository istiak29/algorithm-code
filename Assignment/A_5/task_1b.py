from collections import deque

input_file = open("input_1b.txt", "r")
output_file = open("output_1b.txt", "w")

number_of_course, prerequest = list(map(int, input_file.readline().split()))

graph_list = []
for i in range(number_of_course + 1):
    temp_1 = []
    graph_list.append(temp_1)

for j in range(prerequest):
    temp_2 = input_file.readline().split()
    c1, c2 = int(temp_2[0]), int(temp_2[1])
    graph_list[c1].append(c2)

if number_of_course < prerequest:
    visited = [0] * (prerequest + 1)
    indegree = [0] * (prerequest + 1)
elif prerequest < number_of_course:
    visited = [0] * (number_of_course + 1)
    indegree = [0] * (number_of_course + 1)
else:
    visited = [0] * (number_of_course + 1)
    indegree = [0] * (number_of_course + 1)

flag = False
order_list = []
queue = deque()
for i in range(1, number_of_course + 1):
    for j in graph_list[i]:
        indegree[j] += 1
for i in range(1, number_of_course + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    value = queue.popleft()
    order_list.append(value)
    for n in graph_list[value]:
        if indegree[n] != 0:
            indegree[n] -= 1
        if indegree[n] == 0:
            queue.append(n)
if len(order_list) != number_of_course:
    flag = True

if flag:
    print('IMPOSSIBLE', file=output_file)
else:
    print(order_list, file=output_file)

output_file.close()
