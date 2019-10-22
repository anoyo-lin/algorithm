#!/usr/bin/python3
def bin_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high)//2
        if sorted_list[mid] < target:
            high = mid - 1
        elif sorted_list[mid] > target:
            low = mid + 1
        else:
            if sorted_list[mid] == target:
                print ('found it at index {0}'.format(mid))
                return True
    return False

def bfs(start_name):
    from collections import deque
    search_queue = deque()
    searched = []

    search_queue  += graph[start_name]

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if is_seller(person):
                print ('{0} is the seller'.format(person))
                return True
            else:
                search_queue +=graph[person]
                searched.append(person)
    return False

