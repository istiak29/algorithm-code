file_input = open('input_3.txt', 'r')

arr = list(map(lambda x: int(x), file_input.readline().split(',')))

print(arr)
