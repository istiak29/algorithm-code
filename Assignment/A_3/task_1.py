def merge(arr1, arr2):
    new_array = []
    i, j = 0, 0
    count = 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            new_array.append(arr1[i])
            i += 1
        else:
            new_array.append(arr2[j])
            j += 1

            count += len(arr1) - i

    if i < len(arr1):
        new_array += arr1[i:]

    elif j < len(arr2):
        new_array += arr2[j:]

    return count


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    else:

        mid = len(arr) // 2

        arr1 = mergeSort(arr[:mid])
        arr2 = mergeSort(arr[mid:])

        return merge(arr1, arr2)


input_file = open("input_1.txt", "r")
output_file = open("output_1.txt", "w")

line = int(input_file.readline())

array = list(map(int, input_file.readline().split(' ')))


count = mergeSort(array)

print(count)
