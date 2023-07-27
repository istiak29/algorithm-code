def binarySearch(array, key):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == key:
            return f"Found at index: {mid}, and the value is: {array[mid]}"
        elif key > array[mid]:
            left = mid + 1
        elif key < array[mid]:
            right = mid - 1
    return f"{key} is Not Found"


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
s = 19
print(binarySearch(a, s))
