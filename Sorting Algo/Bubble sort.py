def bubbleSort(array):
    flag = False
    for step in range(len(array)):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
            flag = True
        if flag == False:  # if not flag:
            break
    return array


n = [5, 4, 12, 11, 9]
print("The sorted array is (accending)", bubbleSort(n))
