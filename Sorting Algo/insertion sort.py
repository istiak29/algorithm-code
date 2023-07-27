def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]

        i = step - 1
        while i >= 0 and key < array[i]:
            array[i + 1] = array[i]
            i -= 1

        array[i + 1] = key  # after finished the loop i will always 0 and the lowest value will sit 0th index

    return array


a = [43, 31, 26, 29, 12]
a = [2, 5, 1.2, 6.7, 1.7, 9.3, 2.2, 7.7, 0, -4, -5.1, 2, 5, 5.2]
print(insertionSort(a))
