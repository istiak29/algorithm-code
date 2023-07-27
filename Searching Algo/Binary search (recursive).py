def binarySearch(array, key, left, right):
    if right >= left:
        mid = (left + right) // 2

        if array[mid] == key:
            return f"Found at index: {mid}, and the value is: {array[mid]}"
        elif key > array[mid]:
            return binarySearch(array, key, mid + 1, right)
        elif key < array[mid]:
            return binarySearch(array, key, left, mid - 1)
    else:
        return f"{key} is Not Found"


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

s = 14
print(binarySearch(a, s, 0, len(a)-1))
