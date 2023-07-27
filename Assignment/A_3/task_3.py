def quickSort(array, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(array) - 1

    if left < right:
        t_pivot = partition(array, left, right)

        quickSort(array, left, t_pivot - 1)
        quickSort(array, t_pivot + 1, right)

    return array


def partition(array, left, right):
    pivot = array[right]
    l = left - 1

    for r in range(left, right):

        if array[r] <= pivot:
            l += 1
            array[l], array[r] = array[r], array[l]

    array[l + 1], array[right] = array[right], array[l + 1]

    return l + 1


input_file = open("input_2.txt", "r")
output_file = open("output_2.txt", "w")

testNum = int(input_file.readline())
array = list(map(int, input_file.readline().split(' ')))

sortedArray = quickSort(array)

sorted_string = list(map(str, sortedArray))

output_file.write(' '.join(sorted_string))
