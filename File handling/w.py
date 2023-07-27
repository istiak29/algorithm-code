age = input("Enter your age: ")
f = open('age.txt', 'w')
f.write(age)
f.write('\n15')
# print(f.read())
f.close()


f = open('age.txt', 'r')
print(f.read())
f.close()









