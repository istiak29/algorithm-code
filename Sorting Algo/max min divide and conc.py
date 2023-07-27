def max_min_finder(array, left, right):
    if left == right:
        return array[left], array[right]
    if left == right - 1:
        # if array[left] > array[right]:
        #     return array[left], array[right]
        # else:
        #     return array[right], array[left]
        return (array[left], array[right]) if array[left] > array[right] else (array[right], array[left])

    mid = (left + right) // 2

    left_max, left_min = max_min_finder(array, left, mid)

    right_max, right_min = max_min_finder(array, mid + 1, right)

    final_max = max(left_max, right_max)

    final_min = max(left_min, right_min)

    return final_max, final_min


a = [6, 4, 3, 1, 16, 2, 19, 7, 17]
l = 0
r = len(a) - 1

maximum, minimum = max_min_finder(a, l, r)

print(f"Max Number is {maximum} and Min Number is {minimum}")

