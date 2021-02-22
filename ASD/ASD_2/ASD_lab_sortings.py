def partition(array, low, high):
    i = (low-1)
    pivot = array[high]

    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            array[i],array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return(i+1)

def quicksort_func(array, low, high):
    if len(array) == 1:
        return array
    elif low < high:
        part_index = partition(array, low, high)

        quicksort_func(array, low, part_index-1)
        quicksort_func(array,part_index+1, high)
    return array