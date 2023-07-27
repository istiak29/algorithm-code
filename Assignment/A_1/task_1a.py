input_file = open('input1a.txt', 'r')
output_file = open('output1a.txt', 'w')
line_number = int(input_file.readline().strip())
print(line_number)
for i in range(line_number):
    number = int(input_file.readline().strip())
    if number%2 == 0:
        output_file.write(f'{number} is a even Number.\n')
    else:
        output_file.write(f'{number} is a odd Number.\n')
