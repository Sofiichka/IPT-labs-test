#powered by Baltazaer1697
from random import randint
import time

#addition function for quick sort, which divide list in parts 
def partition(array, low, high):
    global swaps
    i = (low-1) 
    pivot = array[high] #last element in list
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            array[i],array[j] = array[j], array[i]
            swaps+=1 #swap elements
    array[i+1], array[high] = array[high], array[i+1] 
    swaps+=1
    return(i+1)

#quicksort function
def quicksort_func(array, low, high):
    if len(array) == 1:
        return array
    elif low < high:
        part_index = partition(array, low, high)
        quicksort_func(array, low, part_index-1) #sorting every left half of list
        quicksort_func(array,part_index+1, high) #sorting every right half of list
    return array
    
#buble sort fucntion
def buble_sort_func(array):
    global swaps
    for i in range(len(array)-1):
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swaps+=1
    return array

swaps = 0
final_time = 0
#loop testing quicksorting
for x in range(0,10):
    testing_list = [randint(0,120) for x in range (0,100)]
    start_time = time.time()
    quicksort_func(testing_list,0,len(testing_list)-1)
    final_time += time.time()-start_time
print("Average time for quicksort  = ", final_time/10)  #average time for sorting on 10 lists
print("Swap actions during sorting ", swaps)            #counters swap actions during sorting


swaps = 0
final_time = 0
#loop testing buble sorting
for x in range(0,10):
    testing_list = [randint(0,120) for x in range (0,100)]
    start_time = time.time()
    buble_sort_func(testing_list)
    final_time += time.time()-start_time
print("Average time for buble sort = ", final_time/10)  #average time for sorting on 10 lists
print("Swap actions during sorting ", swaps)            #counters swap actions during sorting
