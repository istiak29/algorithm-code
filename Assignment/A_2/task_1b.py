input_file = open("input_1b.txt", "r")
output_file = open("output_1b.txt", "w")

test_num, sumVal = list(map(int, input_file.readline().split(" ")))
num = list(map(int, input_file.readline().split(" ")))

prev_num = {}

flag = "IMPOSSIBLE"

for i in range(test_num):
    if num[i] in prev_num:
        flag = f'{prev_num[num[i]] + 1} {i + 1}'
        break
    else:
        prev_num[sumVal - num[i]] = i

output_file.write(flag)

input_file.close()
output_file.close()
