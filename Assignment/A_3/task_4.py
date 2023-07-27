def Kfinder(array, k, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(array) - 1

    if k > 0 and k <= right + 1:

        t_pivot = partitionFork(array, left, right)

        if t_pivot == k - 1:
            return array[t_pivot + 1]

        elif t_pivot > k - 1:
            return Kfinder(array, k, left, t_pivot - 1)

        return Kfinder(array, k, t_pivot + 1, right)

    print("Out of bound")
    return None


def partitionFork(array, left, right):
    pivot = array[right]
    i = left - 1

    for j in range(left, right):

        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]

    return i + 1


input_file = open("input_4.txt", "r")
output_file = open("output_4.txt", "w")

testNum = int(input_file.readline())
array = list(map(int, input_file.readline().split(' ')))

while True:
    k = int(input_file.readline())
    if k is not None:
        kth_value = Kfinder(array, k)
        output_file.write(f'{k}th is  {kth_value}')
    break




