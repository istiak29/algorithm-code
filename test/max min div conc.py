def find_max_min(arr, left, right):
    if left == right:
        # Base case: Only one element in the array
        return arr[left], arr[right]

    if right == left + 1:
        # Base case: Two elements in the array
        return (arr[left], arr[right]) if arr[left] > arr[right] else (arr[right], arr[left])

    mid = (left + right) // 2

    # Divide the array into two halves
    max_left, min_left = find_max_min(arr, left, mid)
    max_right, min_right = find_max_min(arr, mid + 1, right)

    # Combine the results to find overall maximum and minimum
    overall_max = max(max_left, max_right)
    overall_min = min(min_left, min_right)

    return overall_max, overall_min


# Example usage:
arr = [7, 3, 11, 5, 9, 13, 1, 15, 17, 19]
max_num, min_num = find_max_min(arr, 0, len(arr) - 1)

print("Maximum number:", max_num)
print("Minimum number:", min_num)
