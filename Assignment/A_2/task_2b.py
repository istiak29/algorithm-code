def merge(arr1, arr2):
    new_array = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] > arr2[j]:
            new_array.append(arr2[j])
            j += 1
        else:
            new_array.append(arr1[i])
            i += 1

    if i < len(arr1):
        new_array += arr1[i:]

    elif j < len(arr2):
        new_array += arr2[j:]

    return new_array


input_file = open("input_2b.txt", "r")
output_file = open("output_2b.txt", "w")

testNum_1 = int(input_file.readline())
arr_1 = list(map(int, input_file.readline().split(' ')))

testNum_2 = int(input_file.readline())
arr_2 = list(map(int, input_file.readline().split(' ')))

sortedArray = merge(arr_1, arr_2)

sorted_string = list(map(str, sortedArray))

output_file.write(' '.join(sorted_string))

input_file.close()
output_file.close()
