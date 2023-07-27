# Task 1


input_file = open("input_1a.txt", "r")
output_file = open("output_1a.txt", "w")

idxVal = list(map(int, input_file.readline().split(" ")))
num = list(map(int, input_file.readline().split(" ")))

flag = "IMPOSSIBLE"

for i in range(idxVal[0]):
    for j in range(i+1, idxVal[0]):

        if num[i] + num[j] == idxVal[1]:
            flag = f'{i + 1} {j + 1}'
            break
    if flag != "IMPOSSIBLE":
        break

output_file.write(flag)


output_file.close()