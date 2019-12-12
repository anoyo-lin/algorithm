#!/usr/bin/python3
lst = [ 2, 7, 3, 2, 1, 0, 11, 64 ]
def quick_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = len(lst)//2
        less = [ x for x in lst[:pivot] if x <= lst[pivot] ] + [ x for x in lst[pivot+1:] if x <= lst[pivot] ]
        more = [ x for x in lst[:pivot] if x > lst[pivot] ] + [ x for x in lst[pivot+1:] if x > lst[pivot] ]
        return less + [lst[pivot]] + more

print (quick_sort(lst))

def binary_search(sorted_lst, target):
    low = 0 
    high = len(sorted_lst) - 1
    while low <= high:
        mid = ( low + high )//2
        if sorted_lst[mid] < target:
            low = mid + 1
        elif sorted_lst[mid] > target:
            high = mid - 1
        else:
            print (mid)
            return True
    return False

print (binary_search(quick_sort(lst), 11))
