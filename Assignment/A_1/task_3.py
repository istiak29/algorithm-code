input_file = open("input_3.txt", "r")
output_file = open("output_3.txt", "w")

test_case = int(input_file.readline())

sid = input_file.readline()
st_ID = list(map(int, sid.split()))

m = input_file.readline()
marks = list(map(int, m.split()))

for i in range(test_case - 1):
    flag = True
    for j in range(test_case - 1 - i):
        if marks[j] < marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]
            st_ID[j], st_ID[j + 1] = st_ID[j + 1], st_ID[j]
            flag = False

        elif marks[j] == marks[j + 1]:
            if st_ID[j] > st_ID[j + 1]:
                st_ID[j], st_ID[j + 1] = st_ID[j + 1], st_ID[j]
            flag = False

        if flag == True:
            break

for k in range(test_case):
    output_file.write(f"ID: {st_ID[k]} Mark: {marks[k]}\n")

output_file.close()