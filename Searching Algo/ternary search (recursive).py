def Ternary_Search(l, r, array, key):
    if l <= r:
        mid1 = (l + (r - l) // 3)
        mid2 = (r - (r - l) // 3)

        if key == array[mid1]:
            if key == array[mid1]:
                return f"Found at index {mid1} and key is {array[mid1]}"
            elif key == array[mid2]:
                return f"Found at index {mid2} and key is {array[mid2]}"
            elif key < array[mid1]:
                # r = mid1 - 1
                return Ternary_Search(l, mid1 - 1, array, key)
            elif key > array[mid2]:
                # l = mid2 + 1
                return Ternary_Search(mid2 + 1, r, array, key)
            else:
                # l = mid1 + 1
                # r - mid2 - 1
                return Ternary_Search(mid1 + 1, mid2 - 1, array, key)
    else:
        return "NOT Found"


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 27, 29, 31, 39, 49]
k = 17
left = 0
right = len(a) - 1

print(Ternary_Search(left, right, a, k))
