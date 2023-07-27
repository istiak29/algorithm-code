def selectionSort(array):
    for step in range(len(array)):
        min_idx = step
        for i in range(step+1, len(array)):
            if array[i] < array[min_idx]:
                min_idx = i

        temp = array[step]
        array[step] = array[min_idx]
        array[min_idx] = temp
    return array


n = [20, 12, 10, 15, 2]
print(selectionSort(n))

