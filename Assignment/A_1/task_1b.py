input_file = open("input1b.txt", "r")
output_file = open("output1b.txt", "w")
line_number = int(input_file.readline().strip())

for i in range(line_number):
    temp = input_file.readline()
    temp = temp.strip()
    string_equation = temp.replace("calculate", '')
    calc = str(eval(string_equation))
    output_file.write(f"The result of {string_equation} is {calc}\n")

output_file.close()


