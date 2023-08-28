# this task number is 1 for summer 2023 in assignment 8
# this task number is 3 for spring 2023
# task3
input_file = open('input_1.txt', 'r')
output_file = open('output_1.txt', 'w')

list1 = input_file.readline().split()

ver = int(list1[0])
edg = int(list1[1])

list2 = []
for val1 in range(edg):
    a, b, c = input_file.readline().split()
    list2.append([int(a), int(b), int(c)])


def union(l3, l4, n1, n2):
    value1 = find(l3, n1)
    value2 = find(l3, n2)
    if l4[value1] < l4[value2]:
        l3[value1] = value2
    elif l4[value1] > l4[value2]:
        l3[value2] = value1
    else:
        l3[value2] = value1
        l4[value1] += 1


def find(l3, numb):
    if l3[numb] == numb:
        return numb
    return find(l3, l3[numb])


result = []
v1, v2 = 0, 0
summation = 0
list2 = sorted(list2, key=lambda item: item[2])
list3 = []
list4 = [0] * (ver + 1)

for val2 in range(ver + 1):
    list3.append(val2)

while v2 < ver - 1:
    ver1, ver2, wei = list2[v1]
    v1 += 1
    numb1 = find(list3, ver1)
    numb2 = find(list3, ver2)
    if numb1 != numb2:
        v2 += 1
        result.append([ver1, ver2, wei])
        union(list3, list4, numb1, numb2)

for val3 in result:
    summation += val3[2]
print(summation, file = output_file)




output_file.close()
