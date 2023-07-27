def insertion(array):
    c = 0
    for i in range(len(array)):
        flag = False
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
                flag = True
        if flag == False:
                break
        c += 1



# a = [2, 5, 9, 23, 1, 34, 3, 29, 8]
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [6, 5, 4, 3, 2, 1]
print(insertion(a))
