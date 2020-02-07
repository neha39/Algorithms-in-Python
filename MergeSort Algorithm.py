def merge(array, low, mid, high):
    """
    1. Here 'array' is the array whose sorted left half and sorted right half 
    elements are to be merged resulting in sorted array as a whole.
    """
    
    i = low
    j = mid + 1
    copy = []
    
    while i <= mid and j <= high:
        if array[i] <= array[j]:
            copy.append(array[i])
            i += 1
        else:
            copy.append(array[j])
            j += 1
            
    if i > mid:
        while j <= high:
            copy.append(array[j])
            j += 1
    else:
        while i <= mid:
            copy.append(array[i])
            i += 1
            
    y = 0
    for x in range(low, high + 1):
        array[x] = copy[y]
        y += 1
    
def merge_sort(array, low, high):
    """
    1. Here 'array' is the array to be sorted.
    2. 'low' and 'high' are the index of first and last element in array respectively.
    3. The function sorts the array passed.
    """
    
    if low < high:
        mid = (low + high) // 2
        merge_sort(array, low, mid)
        merge_sort(array, mid + 1, high)
        merge(array, low, mid, high)
        
""" 
EXAMPLE TO TRY:

arr = [1, 3, 5, 2, 4, 6]
merge_sort(arr, 0, len(arr) - 1)
print(arr)
"""

        
        
