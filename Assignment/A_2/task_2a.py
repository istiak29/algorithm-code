def merge(arr1, arr2):

    new_Array = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] > arr2[j]:
            new_Array.append(arr2[j])
            j += 1
        else:
            new_Array.append(arr1[i])
            i += 1

    if i < len(arr1):
        new_Array += arr1[i:]

    elif j < len(arr2):
        new_Array += arr2[j:]

    return new_Array


def mergeSort(array):

    if len(array) <= 1:
        return array

    else:

        mid = len(array) // 2

        arr1 = mergeSort(array[:mid])
        arr2 = mergeSort(array[mid:])

        return merge(arr1, arr2)


input_file = open("input_2a.txt", "r")
output_file = open("output_2a.txt", "w")

testNum_1 = int(input_file.readline())
arr_1 = list(map(int, input_file.readline().split(' ')))

testNum_2 = int(input_file.readline())
arr_2 = list(map(int, input_file.readline().split(' ')))

mainArray = arr_1 + arr_2

sortedArray = mergeSort(mainArray)

sorted_string = list(map(str, sortedArray))

output_file.write(' '.join(sorted_string))

input_file.close()
output_file.close()