def quicksort(arr):
    if len(arr) < 2: #base case
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr [1:] if i <= pivot]
        greater = [i for i in arr [1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([9,7,5,4,3,12,11,5]))

    