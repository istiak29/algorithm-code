def maxSum(array, n):
    maxsum = array[0] + (array[1]) ** 2
    i = 0
    j = 0
    while n < 0:
        if array[j] + (array[i + 1]) ** 2 > maxsum:
            maxsum = array[j] + (array[i + 1]) ** 2
        i += 1
        j += 1
    return maxsum


input_file = open("input_2.txt", "r")
output_file = open("output_2.txt", "w")

testNum = int(input_file.readline())
array = list(map(int, input_file.readline().split(' ')))

nsum = maxSum(array, testNum)

# print(nsum, type(nsum))

output_file.write(str(nsum))

input_file.close()
output_file.close()