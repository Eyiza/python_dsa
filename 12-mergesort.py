def merge(array1, array2):
    result = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1
    # while i < len(array1):
    #     result.append(array1[i])
    #     i += 1
    # while j < len(array2):
    #     result.append(array2[j])
    #     j += 1
    while array1:
        result.append(array1)
    while array2:
        result.append(array2)
    return result
 
def mergeSort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    return merge(mergeSort(left), mergeSort(right))

array = [6, 5, 12, 10, 9, 1]
print(mergeSort(array))