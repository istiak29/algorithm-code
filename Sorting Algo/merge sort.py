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


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)
