#Uses python3

import sys
def special_merge(left_sort, right_sort):
    i = 0
    j = 0
    combine_sort = []
    
    while i < len(left_sort) and j < len(right_sort):
        if int(left_sort[i] + right_sort[j]) >= int(right_sort[j] + left_sort[i]):
            combine_sort.append(left_sort[i])
            i += 1 
        else:
            combine_sort.append(right_sort[j])
            j += 1 
    
    if i == len(left_sort):
        while j < len(right_sort):
            combine_sort.append(right_sort[j])
            j += 1 
            
    if j == len(right_sort):
        while i <len(left_sort):
            combine_sort.append(left_sort[i]) 
            i += 1 
            
    return combine_sort

def special_merge_sort(numbers):
    if len(numbers) == 1:
        return numbers 
    else:
        mid = len(numbers) // 2
        left_sort = special_merge_sort(numbers[ : mid])
        right_sort = special_merge_sort(numbers[mid : ])
        return special_merge(left_sort, right_sort)

def largest_number(a):
    a = special_merge_sort(a)
    res = ""
    for x in a:
        res += x
    return res
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
