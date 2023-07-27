def partition(arr, low, high):
    # Choose the rightmost element as the pivot
    pivot = arr[high]
    # Index of the smaller element
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            # Increment the index of the smaller element
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Swap arr[i+1] and arr[high] (pivot)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # Partition the array, and get the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort elements before and after the pivot index
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


# Example usage:
arr = [7, 3, 11, 5, 9, 13, 1, 15, 17, 19]
n = len(arr)
quick_sort(arr, 0, n - 1)
print(arr)
