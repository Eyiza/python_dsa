def selection_sort(array):
    n = len(array)
    # Traverse through all array elements
    for i in range(n):
    # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if array[min_idx] > array[j]:
                min_idx = j
        # Swap the found minimum element with the first element
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


array = [5, 2, 9, 1, 5]
print(selection_sort(array))