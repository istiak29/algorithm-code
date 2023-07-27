''' θ(n) was achieved by keeping a flag and checking that flag after every iteration to see
    if the array is fully sorted or not.'''


def bubbleSort(array):
    for i in range(len(array) - 1):
        flag = True

        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = False

        if flag == True:
            break

    return array


input_file = open("input_2.txt", "r")
output_file = open("output_2.txt", "w")

testCase = int(input_file.readline())
number = input_file.readline()
arr = list(map(int, number.split(" ")))

sorted_array = " ".join(list(map(str, bubbleSort(arr))))

output_file.write(sorted_array)

output_file.close()
