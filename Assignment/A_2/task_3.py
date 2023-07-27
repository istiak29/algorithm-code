def merge(arr1, arr2):

    new_Array = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] > arr2[j]:
            new_Array.append(arr2[j])
            j += 1
        else:
            new_Array.append(arr1[i])
            i += 1

    if i < len(arr1):
        new_Array += arr1[i:]

    elif j < len(arr2):
        new_Array += arr2[j:]

    return new_Array
       # write your code here
     	 # Here a and b are two sorted list
       # merge function will return a sorted list after merging a and b


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])  # write the parameter
        a2 = mergeSort(arr[mid:])  # write the parameter
        return merge(a1, a2)          # complete the merge function above


input_file = open("input_3.txt", "r")
output_file = open("output_3.txt", "w")

testNum = int(input_file.readline())
num = list(map(int, input_file.readline().split(' ')))

sortednum = mergeSort(num)

sorted_string = list(map(str, sortednum))

output_file.write(' '.join(sorted_string))

input_file.close()
output_file.close()