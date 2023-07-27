f = open("myfile.txt", 'r')
text = f.read(5)
print(text)
for i in text:
    print(i)
f.close()