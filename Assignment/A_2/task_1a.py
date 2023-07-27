
input_file = open("input_1a.txt", "r")
output_file = open("output_1a.txt", "w")

test_num, sumVal = list(map(int, input_file.readline().split(" ")))
num = list(map(int, input_file.readline().split(" ")))

flag = "IMPOSSIBLE"

for i in range(test_num):
    for j in range(i+1, test_num):

        if num[i] + num[j] == sumVal:
            flag = f'{i + 1} {j + 1}'
            break
    if flag != "IMPOSSIBLE":
        break

output_file.write(flag)

input_file.close()
output_file.close()