input_file = open("input_4.txt", "r")
output_file = open("output_4.txt", "w")

test_case = int(input_file.readline())

temp_list = list(map(lambda value: value.strip(), input_file.readline()))


def splitterArray(array):
    temp = array.split()
    trname = [temp[0]]
    trtime = list(map(int, (temp[-1].split(":"))))
    return trname + trtime


info_list = list(map(splitterArray, temp_list))


for i in range(test_case - 1):

    flag = True

    for j in range(test_case - i - 1):

        if info_list[j][0] > info_list[j + 1][0]:

            info_list[j], info_list[j + 1] = info_list[j + 1], info_list[j]
            temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]

            flag = False

        elif info_list[j][0] == info_list[j + 1][0]:

            if info_list[j][1] < info_list[j + 1][1]:

                info_list[j], info_list[j + 1] = info_list[j + 1], info_list[j]
                temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]

            elif info_list[j][1] == info_list[j + 1][1]:

                if info_list[j][2] < info_list[j + 1][2]:

                    info_list[j], info_list[j + 1] = info_list[j + 1], info_list[j]
                    temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]

            flag = False

    if flag == True:
        break

for k in range(test_case):
    output_file.write(temp_list[k]+"\n")

output_file.close()