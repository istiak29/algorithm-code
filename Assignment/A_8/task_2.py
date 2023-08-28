def steps(n):
    if n == 1:
        return n
    n1 = 1
    n2 = 2
    for val in range(3, n + 1):
        temp = n1
        n1 = n2
        n2 = temp + n2
    return n2


input_file = open('input_2.txt', 'r')
output_file = open('output_2.txt', 'w')

numb = int(input_file.readline())
result = steps(numb)

print(result, file=output_file)
output_file.close()
