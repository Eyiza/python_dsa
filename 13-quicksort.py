def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp


def pivot(array, pivotIndex=0, endIndex=None):
    if endIndex is None:
        endIndex = len(array) - 1
    swapIndex = pivotIndex
    for i in range(pivotIndex + 1, endIndex + 1):
        if array[i] < array[pivotIndex]:
            swapIndex += 1
            swap(array, i, swapIndex)
    swap(array, pivotIndex, swapIndex)
    return swapIndex

def quickSort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    if left < right:
        pivotIndex = pivot(array, left, right)
        quickSort(array, left, pivotIndex - 1)
        quickSort(array, pivotIndex + 1, right)
    return array


array = [6, 5, 12, 10, 9, 1]
print(quickSort(array))