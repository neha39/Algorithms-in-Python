def merge_count_split_inv(array, low, mid, high):
    """
    1. Here 'array' is the array whose sorted left half and sorted right half 
    elements are to be merged resulting in sorted array as a whole.
    2. It returns count for split inversions.
    """
    
    i = low
    j = mid + 1
    copy = []
    
    split_inv_count = 0
    flag = len(array[low : mid+1])
    
    while i <= mid and j <= high:
        if array[i] <= array[j]:
            copy.append(array[i])
            flag -= 1
            i += 1
        else:
            copy.append(array[j])
            split_inv_count += flag
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
        
    return split_inv_count
    
def sort_count_inv(array, low, high):
    """
    1. Here 'array' is the array to be sorted.
    2. 'low' and 'high' are the index of first and last element in array respectively.
    3. The function sorts the array passed.
    4. It returns count for inversions.
    """
    if low == high:
        return 0
        
    elif low < high:
        mid = (low + high) // 2
        
        l_inv_count = sort_count_inv(array, low, mid)
        r_inv_count = sort_count_inv(array, mid + 1, high)
        split_inv_count = merge_count_split_inv(array, low, mid, high)
        
        return l_inv_count + r_inv_count + split_inv_count
        
"""
EXAMPLE TO TRY:

arr = [6, 5, 4, 3, 2, 1]
inv_count = sort_count_inv(arr, 0, len(arr) - 1)
print(inv_count)
"""

        
        
