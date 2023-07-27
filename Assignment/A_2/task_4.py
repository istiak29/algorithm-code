def MaxFinder(array):
    if len(array) == 1:
        return array[0]

    mid = len(array) // 2
    arr_1 = array[:mid]
    arr_2 = array[mid:]

    maxOf_arr_1 = MaxFinder(arr_1)
    maxOf_arr_2 = MaxFinder(arr_2)

    return max(maxOf_arr_1, maxOf_arr_2)


input_file = open("input_4.txt", "r")
output_file = open("output_4.txt", "w")

testNum = int(input_file.readline())
num = list(map(int, input_file.readline().split(' ')))

maxNum = MaxFinder(num)

output_file.write(str(maxNum))

input_file.close()
output_file.close()

'''
    The time complexity of this code is O(n)
'''