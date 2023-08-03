from collections import deque

input_file = open("input_2.txt", "r")
output_file = open("output_2.txt", "w")


number_of_course, prerequest = list(map(int, input_file.readline().split()))

graph_list = []

start = []
end = []

for val1 in range(number_of_course + 1):
    temp_1 = []
    graph_list.append(temp_1)
for val2 in range(prerequest):
    temp_2 = input_file.readline().split()
    c1, c2 = int(temp_2[0]), int(temp_2[1])
    if c1 not in start:
        start.append(c1)
    if c2 not in end:
        end.append(c2)
    graph_list[c1].append(c2)

if number_of_course < prerequest:
    visited = [0] * (prerequest + 1)
    indeg = [0] * (prerequest + 1)
elif prerequest < number_of_course:
    visited = [0] * (number_of_course + 1)
    indeg = [0] * (number_of_course + 1)
else:
    visited = [0] * (number_of_course + 1)
    indeg = [0] * (number_of_course + 1)

flag = False
s_list = []
sequence = []
queue = deque()

for i in range(1, number_of_course + 1):
    for j in graph_list[i]:
        indeg[j] += 1
for i in range(1, number_of_course + 1):
    if indeg[i] == 0:
        queue.append(i)

while queue:
    value = queue.popleft()
    s_list.append(value)
    for i in graph_list[value]:
        if indeg[i] != 0:
            indeg[i] -= 1
        if indeg[i] == 0:
            queue.append(i)
if len(s_list) != number_of_course:
    flag = True

# pointer
i = 0
j = 0
k = 0

if flag:
    print('IMPOSSIBLE', file=output_file)
else:
    while k < len(s_list):
        if k == 0:
            sequence.append(s_list[k])
            i += 1
        elif i < len(start) and j < len(end):
            if j <= i:
                if end[j] == start[i]:
                    sequence.append(start[i])
                    i += 1
                    j += 1
                elif end[j] < start[i]:
                    sequence.append(end[j])
                    j += 1
                elif j == i:
                    if start[i] < end[j]:
                        sequence.append(start[i])
                        i += 1
                    elif end[j] < start[i]:
                        sequence.append(end[j])
                        j += 1
        elif i < len(start) and j >= len(end):
            sequence.append(start[i])
            i += 1
        elif j < len(end) and i >= len(start):
            sequence.append(end[j])
            j += 1
        k += 1
    print(sequence, file=output_file)


output_file.close()
