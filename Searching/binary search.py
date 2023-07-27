def Bianary_search(left, right, array, key):

    if left <= right:
        mid = (left + right) // 2

    elif array[mid] == key:
        return mid
    elif array[mid] < key:
        right = mid
        return Bianary_search(left, mid+1, array, key)
    elif array[mid] > key:
        left = mid
        return Bianary_search(mid+1, right, array, key)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = 0
r = len(a)-1
k = 7

print(Bianary_search(l, r, a, k))




