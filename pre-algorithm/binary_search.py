#!/usr/bin/python3
sample_lst = [ 1, 3, 6, 10, 12 ]
target = 22 
def binary_search( sorted_lst, target ):
    low = 0
    high = len(sorted_lst) - 1
    while low <= high:
        mid = (low + high)//2
        if sorted_lst[mid] > target:
            high = mid - 1
        elif sorted_lst[mid] < target:
            low = mid + 1
        else:
            if sorted_lst[mid] == target:
                print ("find {0} at index {1}".format(target, mid))
                return True
    print ("can't find {0}".format(target))
    return False

print (binary_search(sample_lst, target))

